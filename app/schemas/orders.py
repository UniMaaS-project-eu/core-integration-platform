from typing import Any, Literal

from pydantic import BaseModel, Field


class OrderIntentRequest(BaseModel):
    user_id: str
    text: str = Field(..., examples=["Create an order for CNC machining capacity next week"])
    context: dict[str, Any] = Field(default_factory=dict)


class OrderIntentResponse(BaseModel):
    order_id: str
    status: Literal["drafted", "pending_chatbot_backend"]
    interpreted_intent: str
    missing_inputs: list[str]

