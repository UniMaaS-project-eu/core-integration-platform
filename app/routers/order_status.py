from fastapi import APIRouter

from app.schemas.workflows import WorkflowListResponse, WorkflowSummary
from app.services import workflow_service
from app.settings import get_settings

router = APIRouter(prefix="/order-status", tags=["order-status"])


@router.get("/workflows", response_model=WorkflowListResponse)
def list_workflows(order_id: str | None = None) -> WorkflowListResponse:
    return workflow_service.list_workflows(order_id=order_id, settings=get_settings())


@router.get("/workflows/{workflow_id}", response_model=WorkflowSummary)
def get_workflow(workflow_id: str) -> WorkflowSummary:
    return workflow_service.get_workflow(workflow_id)

