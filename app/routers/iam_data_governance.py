from fastapi import APIRouter

from app.schemas.iam_data_governance import (
    AuthorizationCheckRequest,
    AuthorizationCheckResponse,
    RegistrationRequest,
    RegistrationResponse,
)
from app.services import iam_data_governance_service

router = APIRouter(prefix="/registration", tags=["ic6-iam-data-governance"])


@router.post("/participants", response_model=RegistrationResponse)
def register_participant(payload: RegistrationRequest) -> RegistrationResponse:
    return iam_data_governance_service.register_participant(payload)


@router.post("/authorize", response_model=AuthorizationCheckResponse)
def authorize(payload: AuthorizationCheckRequest) -> AuthorizationCheckResponse:
    return iam_data_governance_service.authorize(payload)
