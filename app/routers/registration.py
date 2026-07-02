from fastapi import APIRouter

from app.schemas.registration import (
    AuthorizationCheckRequest,
    AuthorizationCheckResponse,
    RegistrationRequest,
    RegistrationResponse,
)
from app.services import registration_service

router = APIRouter(prefix="/registration", tags=["registration"])


@router.post("/participants", response_model=RegistrationResponse)
def register_participant(payload: RegistrationRequest) -> RegistrationResponse:
    return registration_service.register_participant(payload)


@router.post("/authorize", response_model=AuthorizationCheckResponse)
def authorize(payload: AuthorizationCheckRequest) -> AuthorizationCheckResponse:
    return registration_service.authorize(payload)

