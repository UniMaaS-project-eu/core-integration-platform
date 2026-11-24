from fastapi import APIRouter

from app.schemas.federated_catalogue import DatasetFilters, FederatedCatalogueResponse
from app.services import federated_catalogue_service
from app.settings import get_settings

router = APIRouter(prefix="/federated-catalogue", tags=["ic4-federated-catalogue"])


@router.get(
    "",
    response_model=FederatedCatalogueResponse,
    summary="Read Root",
    description="Indicate that the API is running",
)
def read_root() -> FederatedCatalogueResponse:
    return FederatedCatalogueResponse(
        source_status=(
            "Federated Catalogue integration endpoint group. Backend request forwarding is pending."
        ),
    )


@router.post(
    "/datasets",
    response_model=FederatedCatalogueResponse,
    summary="Get Datasets With Optional Filters",
    description="Returns the filtered datasets filtered with the fitlers given in a JSON object.",
)
def get_datasets_with_optional_filters(ds_filters: DatasetFilters | None = None) -> FederatedCatalogueResponse:
    return federated_catalogue_service.get_datasets(ds_filters, settings=get_settings())
