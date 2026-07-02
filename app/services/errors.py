from fastapi import HTTPException

from app.schemas.common import NotImplementedDetail


def missing_contract(component: str, missing_inputs: list[str]) -> None:
    detail = NotImplementedDetail(
        component=component,
        reason="Partner API contract is not defined enough for an executable IC17 proxy.",
        missing_inputs=missing_inputs,
    )
    raise HTTPException(status_code=501, detail=detail.model_dump())

