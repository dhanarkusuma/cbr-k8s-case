from fastapi import APIRouter

from app.models.case_model import KubernetesCase

from app.services.case_service import (
    create_case_service,
    retrieve_case_service,
)

router = APIRouter()


@router.post("/cases")
def create_case(case: KubernetesCase):

    return create_case_service(case)


@router.post("/retrieve")
def retrieve_case(case: KubernetesCase):

    return retrieve_case_service(case)
