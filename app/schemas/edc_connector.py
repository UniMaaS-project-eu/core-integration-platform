from typing import Any, Literal

from pydantic import BaseModel, Field


class AssetRegistrationRequest(BaseModel):
    provider_id: str
    asset_name: str
    manufacturing_domain: str
    description: str
    rdf_service_type: Literal["sparqlendpoint", "httpendpoint", "file"] = "sparqlendpoint"
    metadata: dict[str, Any] = Field(default_factory=dict)


class AssetRegistrationResponse(BaseModel):
    asset_id: str
    status: Literal["drafted", "pending_edc_contract"]
    required_backend: str
    missing_inputs: list[str]

