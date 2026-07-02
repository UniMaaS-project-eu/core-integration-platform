from app.schemas.edc_connector import AssetRegistrationResponse, RdfServiceAssetRegistrationRequest, RdfTransferRequest, RdfTransferResponse
from app.schemas.knowledge_graph import SearchResult
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


def register_rdf_service_asset(payload: RdfServiceAssetRegistrationRequest) -> AssetRegistrationResponse:
    return AssetRegistrationResponse(
        asset_id=payload.asset_id,
        status="pending_edc_deployment",
        service_type=payload.data_address.service_type,
        required_backend="IC1 UniMaaS EDC Connector",
        missing_inputs=[
            "Final EDC management API URL",
            "Authentication mechanism",
            "Exact deployed EDC version",
            "Final UniMaaS dataset property conventions",
        ],
    )


def initiate_rdf_transfer(payload: RdfTransferRequest) -> RdfTransferResponse:
    return RdfTransferResponse(
        asset_id=payload.asset_id,
        status="pending_edc_deployment",
        transfer_type=payload.transfer_type,
        required_backend="IC1 UniMaaS EDC Connector",
        missing_inputs=[
            "Final EDC transfer endpoint URL",
            "Authentication mechanism",
            "Contract negotiation/agreement flow",
            "Runtime policy for RDFSink push versus HttpProxy pull",
        ],
    )
