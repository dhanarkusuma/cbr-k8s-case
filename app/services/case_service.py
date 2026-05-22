from app.models.case_model import KubernetesCase

from app.repositories.case_repository import (
    insert_case,
    get_resolved_cases
)

from app.retrieval.retrieval_engine import retrieve_top_k


def create_case_service(case: KubernetesCase):
    return insert_case(case.model_dump())


def retrieve_case_service(case: KubernetesCase):
    query_case = case.model_dump()
    stored_cases = get_resolved_cases()

    if not stored_cases:
        return {
            "message": "no resolved cases found"
        }

    top_cases = retrieve_top_k(
        query_case,
        stored_cases
    )

    return {
        "top_cases": top_cases
    }
