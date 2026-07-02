from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class NotImplementedDetail(BaseModel):
    component: str
    reason: str
    missing_inputs: list[str]


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    timestamp: datetime
