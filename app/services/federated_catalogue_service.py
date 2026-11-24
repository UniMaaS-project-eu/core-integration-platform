from app.schemas.federated_catalogue import DatasetFilters, FederatedCatalogueResponse
from app.services.configuration import configured
from app.settings import Settings


def _source_status(settings: Settings) -> str:
    if configured(settings.ic4_federated_catalogue_base_url):
        return "Federated Catalogue base URL is configured. Backend request forwarding is pending."
    return (
        "Federated Catalogue route skeleton only. Backend request forwarding is pending. "
        "Configure IC4_FEDERATED_CATALOGUE_BASE_URL and auth before proxying."
    )


def get_datasets(payload: DatasetFilters | None, settings: Settings) -> FederatedCatalogueResponse:
    filters = {} if payload is None else payload.model_dump(by_alias=True, exclude_none=True)
    return FederatedCatalogueResponse(
        source_status=_source_status(settings),
        data={"filters": filters, "datasets": []},
    )
