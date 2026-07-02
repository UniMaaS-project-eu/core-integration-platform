from fastapi import APIRouter

from app.schemas.provider_assets import AssetRegistrationRequest, AssetRegistrationResponse
from app.schemas.search import SearchResult
from app.services import provider_assets_service
from app.settings import get_settings

router = APIRouter(prefix="/provider-assets", tags=["provider-assets"])


@router.get("", response_model=list[SearchResult])
def list_provider_assets(provider_id: str | None = None) -> list[SearchResult]:
    return provider_assets_service.list_provider_assets(provider_id=provider_id, settings=get_settings())


@router.post("", response_model=AssetRegistrationResponse)
def register_provider_asset(payload: AssetRegistrationRequest) -> AssetRegistrationResponse:
    return provider_assets_service.register_provider_asset(payload)

