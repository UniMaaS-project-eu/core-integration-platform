from app.schemas.workflows import WorkflowListResponse, WorkflowSummary
from app.services.configuration import configured
from app.settings import Settings


def list_workflows(order_id: str | None, settings: Settings) -> WorkflowListResponse:
    return WorkflowListResponse(
        workflows=[
            WorkflowSummary(
                workflow_id="workflow-demo-001",
                order_id=order_id or "order-demo-001",
                phase="Unknown",
                progress="0/0",
            )
        ],
        source_status=(
            "Orchestrator base URL is configured. Namespace/auth/selected status fields still need confirmation."
            if configured(settings.ic15_orchestrator_base_url)
            else "Designable from Argo/Kubernetes workflow state. Configure IC15_ORCHESTRATOR_BASE_URL."
        ),
        missing_inputs=["Namespace list", "Auth token flow", "Selected workflow fields"],
    )


def get_workflow(workflow_id: str) -> WorkflowSummary:
    return WorkflowSummary(
        workflow_id=workflow_id,
        phase="Unknown",
        progress="0/0",
    )
