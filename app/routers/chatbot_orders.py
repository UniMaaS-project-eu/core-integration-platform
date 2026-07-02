from fastapi import APIRouter

from app.schemas.orders import OrderIntentRequest, OrderIntentResponse
from app.services import orders_service

router = APIRouter(prefix="/chatbot-orders", tags=["chatbot-orders"])


@router.post("", response_model=OrderIntentResponse)
def create_order_intent(payload: OrderIntentRequest) -> OrderIntentResponse:
    return orders_service.create_order_intent(payload)


@router.get("/{order_id}", response_model=OrderIntentResponse)
def get_order_intent(order_id: str) -> OrderIntentResponse:
    return orders_service.get_order_intent(order_id)

