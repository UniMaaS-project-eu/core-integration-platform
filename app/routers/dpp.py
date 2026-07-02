from fastapi import APIRouter

from app.schemas.dpp import DppProduct, DppProductResponse, DppProductUpsertRequest
from app.services import dpp_service
from app.settings import get_settings

router = APIRouter(prefix="/dpp", tags=["dpp"])


@router.get("/products", response_model=list[DppProduct])
def list_dpp_products() -> list[DppProduct]:
    return dpp_service.list_dpp_products()


@router.get("/products/{product_id}", response_model=DppProductResponse)
def get_dpp_product(product_id: str) -> DppProductResponse:
    return dpp_service.get_dpp_product(product_id, settings=get_settings())


@router.post("/products", response_model=DppProductResponse)
def create_dpp_product(payload: DppProductUpsertRequest) -> DppProductResponse:
    return dpp_service.create_dpp_product(payload)


@router.patch("/products/{product_id}", response_model=DppProductResponse)
def update_dpp_product(product_id: str, payload: DppProductUpsertRequest) -> DppProductResponse:
    return dpp_service.update_dpp_product(product_id, payload)

