from fastapi import APIRouter

from app.schemas.edc_connector import (
    AssetRegistrationResponse,
    RdfServiceAssetRegistrationRequest,
    RdfTransferRequest,
    RdfTransferResponse,
)
from app.schemas.knowledge_graph import SearchResult
from app.services import edc_connector_service
from app.settings import get_settings

router = APIRouter(prefix="/provider-assets", tags=["ic1-edc-connector"])


@router.get("", response_model=list[SearchResult])
def list_provider_assets(provider_id: str | None = None) -> list[SearchResult]:
    return edc_connector_service.list_provider_assets(provider_id=provider_id, settings=get_settings())


@router.post("", response_model=AssetRegistrationResponse)
def register_rdf_service_asset(payload: RdfServiceAssetRegistrationRequest) -> AssetRegistrationResponse:
    return edc_connector_service.register_rdf_service_asset(payload)


@router.post("/transfers", response_model=RdfTransferResponse)
def initiate_rdf_transfer(payload: RdfTransferRequest) -> RdfTransferResponse:
    return edc_connector_service.initiate_rdf_transfer(payload)
