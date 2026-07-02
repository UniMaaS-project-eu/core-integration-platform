from fastapi import APIRouter

from app.schemas.edc_connector import AssetRegistrationRequest, AssetRegistrationResponse
from app.schemas.knowledge_graph import SearchResult
from app.services import edc_connector_service
from app.settings import get_settings

router = APIRouter(prefix="/provider-assets", tags=["ic1-edc-connector"])


@router.get("", response_model=list[SearchResult])
def list_provider_assets(provider_id: str | None = None) -> list[SearchResult]:
    return edc_connector_service.list_provider_assets(provider_id=provider_id, settings=get_settings())


@router.post("", response_model=AssetRegistrationResponse)
def register_provider_asset(payload: AssetRegistrationRequest) -> AssetRegistrationResponse:
    return edc_connector_service.register_provider_asset(payload)
