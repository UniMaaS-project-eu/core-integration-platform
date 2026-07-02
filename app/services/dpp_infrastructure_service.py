from app.schemas.dpp_infrastructure import DppProduct, DppProductResponse, DppProductUpsertRequest
from app.services.configuration import configured
from app.settings import Settings


def list_dpp_products() -> list[DppProduct]:
    return [
        DppProduct(
            product_id="dpp-demo-001",
            name="Demo DPP product",
            lifecycle_status="placeholder",
            attributes={"contract_status": "partial", "backend": "IC7 DPP Infrastructure"},
        )
    ]


def get_dpp_product(product_id: str, settings: Settings) -> DppProductResponse:
    return DppProductResponse(
        product=DppProduct(product_id=product_id, name="Demo DPP product", lifecycle_status="placeholder"),
        source_status=(
            "DPP base URL is configured. Final DPP API and entity schemas are pending."
            if configured(settings.ic7_dpp_base_url)
            else "NGSI-LD/Orion-LD direction known. Configure IC7_DPP_BASE_URL and provide entity schemas."
        ),
        missing_inputs=["Final DPP entity schemas", "Allowed write operations", "Auth", "Error model"],
    )


def create_dpp_product(payload: DppProductUpsertRequest) -> DppProductResponse:
    product_id = payload.product_id or f"dpp-draft-{payload.name.lower().replace(' ', '-')}"
    return DppProductResponse(
        product=DppProduct(
            product_id=product_id,
            name=payload.name,
            lifecycle_status=payload.lifecycle_status,
            attributes=payload.attributes,
        ),
        source_status="Request accepted as IC17 DTO draft. Final IC7 DPP write contract is pending.",
        missing_inputs=["Final DPP write schema", "Identifier policy", "Auth", "Validation rules"],
    )


def update_dpp_product(product_id: str, payload: DppProductUpsertRequest) -> DppProductResponse:
    return DppProductResponse(
        product=DppProduct(
            product_id=product_id,
            name=payload.name,
            lifecycle_status=payload.lifecycle_status,
            attributes=payload.attributes,
        ),
        source_status="Request accepted as IC17 DTO draft. Final IC7 DPP update contract is pending.",
        missing_inputs=["Final DPP update schema", "Allowed writable fields", "Auth", "Conflict handling"],
    )
