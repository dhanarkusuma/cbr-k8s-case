from sqlalchemy.orm import Session
from models.case_model import KubernetesCase


def get_candidate_cases(
    db,
    pod_status,
    deployment_change,
    node_pressure
):
    return (
        db.query(KubernetesCase)
        .filter(
            KubernetesCase.pod_status
            == pod_status,

            KubernetesCase.deployment_change
            == deployment_change,

            KubernetesCase.node_pressure
            == node_pressure
        )
        .all()
    )

def retain_new_case(db: Session, case_data: dict):
    new_case = KubernetesCase(
        **case_data
    )

    db.add(new_case)
    db.commit()
    db.refresh(new_case)

    return new_case

def update_case_solution(
    db,
    case_id,
    revised_solution,
    revised_root_cause
):
    case = db.query(
        KubernetesCase
    ).filter(
        KubernetesCase.id == case_id
    ).first()

    if not case:
        return None

    case.solution = revised_solution
    case.root_cause = revised_root_cause
    db.commit()

    db.refresh(case)

    return case