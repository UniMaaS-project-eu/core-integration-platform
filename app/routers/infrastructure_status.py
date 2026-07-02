from fastapi import APIRouter

from app.services import infrastructure_service

router = APIRouter(prefix="/infrastructure-status", tags=["infrastructure-status"])


@router.get("/assets")
def infrastructure_assets() -> None:
    return infrastructure_service.list_infrastructure_assets()

