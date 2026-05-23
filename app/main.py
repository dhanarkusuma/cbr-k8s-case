import streamlit as st
import pandas as pd

from config.database import (
    SessionLocal,
    engine
)

from models.case_model import (
    Base
)

from repositories.case_repository import (
    get_candidate_cases,
    retain_new_case,
    update_case_solution
)

from services.retrieval import (
    retrieve_top_k
)

# Run DB Migration
Base.metadata.create_all(
    bind=engine
)

db = SessionLocal()

# Streamlit configs
st.set_page_config(
    page_title="CBR Kubernetes Incident System",
    layout="wide"
)

# Setting pages
st.title(
    "CBR Kubernetes Incident System"
)

st.write(
    """
    Retrieve, Reuse, Revise,
    and Retain Kubernetes incidents
    using Case-Based Reasoning.
    """
)

# Input Form
st.header("Incident Input")
pod_status = st.selectbox(
    "Pod Status",
    [
        "Running",
        "CrashLoopBackOff",
        "Pending",
        "Error",
        "ImagePullBackOff"
    ]
)
cpu_usage = st.slider("CPU Usage",0,100)
memory_usage = st.slider("Memory Usage",0,100)
restart_count = st.number_input("Restart Count", min_value=0)
deployment_change = st.checkbox("Recent Deployment Change")
node_pressure = st.checkbox("Node Pressure")
error_log = st.text_area("Error Log")

if st.button("Retrieve Similar Cases"):
    query_case = {
        "pod_status": pod_status,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "restart_count": restart_count,
        "deployment_change": deployment_change,
        "node_pressure": node_pressure,
        "error_log": error_log
    }

    # Get candidate cases
    candidate_cases = get_candidate_cases(
        db,
        pod_status,
        deployment_change,
        node_pressure
    )


    # Add option retain if no candidates
    if not candidate_cases:
        st.warning("No candidate cases found")
        st.subheader("Retain New Knowledge")

        retain_root_cause = st.text_input("Root Cause")
        retain_solution = st.text_area("Solution")

        if st.button("Retain New Case"):
            new_case = {
                **query_case,
                "root_cause": retain_root_cause,
                "solution": retain_solution
            }

            retain_new_case(db,new_case)
            st.success("New knowledge retained")
    else:

        results = retrieve_top_k(
            query_case,
            candidate_cases
        )

        # Summary similar table
        st.subheader("Similarity Table")
        table_data = []
        for result in results:
            table_data.append({
                "Similarity (%)": round(result["similarity"] * 100, 2),
                "Root Cause": result["root_cause"],
                "Solution": result["solution"]
            })

        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True)



        # Display top similar cases
        st.subheader("Top Similar Cases")
        for idx, result in enumerate(
            results,
            start=1
        ):
            similarity_percent = round(result["similarity"] * 100, 2)
            if similarity_percent >= 90:
                st.success(
                    f"Case #{idx} "
                    f"- Similarity "
                    f"{similarity_percent}%"
                )
            elif similarity_percent >= 70:
                st.warning(
                    f"Case #{idx} "
                    f"- Similarity "
                    f"{similarity_percent}%"
                )
            else:
                st.error(
                    f"Case #{idx} "
                    f"- Similarity "
                    f"{similarity_percent}%"
                )

            with st.expander(f"Detail Case #{idx}"):
                st.write(
                    f"Root Cause: "
                    f"{result['root_cause']}"
                )

                st.write(
                    f"Solution: "
                    f"{result['solution']}"
                )

                st.write(
                    f"Related Log: "
                    f"{result['error_log']}"
                )

                st.markdown("### Revise")

                revised_root_cause = (
                    st.text_input(
                        f"Revised Root Cause #{idx}",
                        value=result[
                            "root_cause"
                        ]
                    )
                )

                revised_solution = (
                    st.text_area(
                        f"Revised Solution #{idx}",
                        value=result[
                            "solution"
                        ]
                    )
                )

                if st.button(f"Save Revision #{idx}"):

                    update_case_solution(
                        db,
                        result["case_id"],
                        revised_solution,
                        revised_root_cause
                    )

                    st.success("Case revised")


        # Retain form section
        st.subheader("Retain As New Knowledge")
        st.info(
            """
            Save this incident as a new case
            into the CBR knowledge base.
            """
        )
        retain_root_cause = st.text_input("Root Cause")
        retain_solution = st.text_area("Solution")

        if st.button("Retain New Knowledge"):
            new_case = {
                **query_case,
                "root_cause": retain_root_cause,
                "solution": retain_solution
            }

            retain_new_case(db, new_case)
            st.success("New knowledge retained successfully")