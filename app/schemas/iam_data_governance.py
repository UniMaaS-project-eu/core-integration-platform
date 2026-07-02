from typing import Literal

from pydantic import BaseModel, Field


class RegistrationRequest(BaseModel):
    organization_name: str = Field(..., examples=["Example Manufacturing Ltd"])
    participant_type: Literal["provider", "consumer"]
    manufacturing_domain: str = Field(..., examples=["aerospace"])
    contact_email: str = Field(..., examples=["user@example.org"])


class RegistrationResponse(BaseModel):
    registration_id: str
    status: Literal["received", "pending_iam_contract"]
    participant_type: Literal["provider", "consumer"]
    required_backend: str
    missing_inputs: list[str]


class AuthorizationCheckRequest(BaseModel):
    subject_id: str
    action: str
    resource: str


class AuthorizationCheckResponse(BaseModel):
    allowed: bool
    decision_source: Literal["placeholder"]
    reason: str
    missing_inputs: list[str]

