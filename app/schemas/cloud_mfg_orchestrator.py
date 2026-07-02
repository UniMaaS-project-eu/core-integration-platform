from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class WorkflowSummary(BaseModel):
    workflow_id: str
    order_id: str | None = None
    phase: Literal["Pending", "Running", "Succeeded", "Failed", "Unknown"]
    started_at: datetime | None = None
    finished_at: datetime | None = None
    progress: str | None = None
    source_component: str = "IC15 Cloud Mfg Orchestrator"


class WorkflowListResponse(BaseModel):
    workflows: list[WorkflowSummary]
    source_status: str
    missing_inputs: list[str]

