from app.schemas.iam_data_governance import (
    AuthorizationCheckRequest,
    AuthorizationCheckResponse,
    RegistrationRequest,
    RegistrationResponse,
)


def register_participant(payload: RegistrationRequest) -> RegistrationResponse:
    return RegistrationResponse(
        registration_id=f"draft-{payload.participant_type}-{payload.organization_name.lower().replace(' ', '-')}",
        status="pending_iam_contract",
        participant_type=payload.participant_type,
        required_backend="IC6 IAM & Data Governance",
        missing_inputs=[
            "Final IAM OpenAPI",
            "Realm/domain mapping",
            "Provider/consumer role assignment rules",
            "Token creation flow",
        ],
    )


def authorize(payload: AuthorizationCheckRequest) -> AuthorizationCheckResponse:
    return AuthorizationCheckResponse(
        allowed=False,
        decision_source="placeholder",
        reason=f"No final IC6 authorization contract is available for action '{payload.action}'.",
        missing_inputs=["Authorization request/response schema", "Policy metadata shape", "Token validation rules"],
    )
