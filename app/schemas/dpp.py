from typing import Any

from pydantic import BaseModel, Field


class DppProduct(BaseModel):
    product_id: str
    name: str
    lifecycle_status: str
    ngsi_ld_type: str = "Product"
    attributes: dict[str, Any] = Field(default_factory=dict)


class DppProductUpsertRequest(BaseModel):
    product_id: str | None = None
    name: str
    lifecycle_status: str
    attributes: dict[str, Any] = Field(default_factory=dict)


class DppProductResponse(BaseModel):
    product: DppProduct
    source_status: str
    missing_inputs: list[str]

