from app.schemas.provider_assets import AssetRegistrationRequest, AssetRegistrationResponse
from app.schemas.search import SearchResult
from app.services.configuration import configured
from app.settings import Settings


def list_provider_assets(provider_id: str | None, settings: Settings) -> list[SearchResult]:
    return [
        SearchResult(
            id="asset-demo-001",
            title="Demo provider asset",
            description="Placeholder provider asset until EDC/Federated Catalogue contracts are finalized.",
            source_component="IC1 UniMaaS EDC Connector / IC4 Federated Catalogue",
            metadata={
                "provider_id": provider_id,
                "contract_status": "partial",
                "edc_configured": configured(settings.ic1_edc_base_url),
                "federated_catalogue_configured": configured(settings.ic4_federated_catalogue_base_url),
            },
        )
    ]


def register_provider_asset(payload: AssetRegistrationRequest) -> AssetRegistrationResponse:
    return AssetRegistrationResponse(
        asset_id=f"draft-asset-{payload.asset_name.lower().replace(' ', '-')}",
        status="pending_edc_contract",
        required_backend="IC1 UniMaaS EDC Connector",
        missing_inputs=[
            "Final EDC management API URL",
            "Authentication mechanism",
            "Exact RDFService registration payload expected by the deployed connector",
            "Supported transfer initiation endpoints",
        ],
    )
