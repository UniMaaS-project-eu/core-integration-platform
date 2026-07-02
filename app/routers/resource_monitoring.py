from fastapi import APIRouter

from app.services import resource_monitoring_service

router = APIRouter(prefix="/infrastructure-status", tags=["ic5-resource-monitoring"])


@router.get("/assets")
def infrastructure_assets() -> None:
    return resource_monitoring_service.list_infrastructure_assets()
