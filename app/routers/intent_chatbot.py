from fastapi import APIRouter

from app.schemas.intent_chatbot import OrderIntentRequest, OrderIntentResponse
from app.services import intent_chatbot_service

router = APIRouter(prefix="/chatbot-orders", tags=["ic11-intent-chatbot"])


@router.post("", response_model=OrderIntentResponse)
def create_order_intent(payload: OrderIntentRequest) -> OrderIntentResponse:
    return intent_chatbot_service.create_order_intent(payload)


@router.get("/{order_id}", response_model=OrderIntentResponse)
def get_order_intent(order_id: str) -> OrderIntentResponse:
    return intent_chatbot_service.get_order_intent(order_id)
