from fastapi import APIRouter

from app.schemas.cloud_mfg_orchestrator import WorkflowListResponse, WorkflowSummary
from app.services import cloud_mfg_orchestrator_service
from app.settings import get_settings

router = APIRouter(prefix="/order-status", tags=["ic15-cloud-mfg-orchestrator"])


@router.get("/workflows", response_model=WorkflowListResponse)
def list_workflows(order_id: str | None = None) -> WorkflowListResponse:
    return cloud_mfg_orchestrator_service.list_workflows(order_id=order_id, settings=get_settings())


@router.get("/workflows/{workflow_id}", response_model=WorkflowSummary)
def get_workflow(workflow_id: str) -> WorkflowSummary:
    return cloud_mfg_orchestrator_service.get_workflow(workflow_id)
