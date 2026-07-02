from app.schemas.orders import OrderIntentRequest, OrderIntentResponse


def create_order_intent(payload: OrderIntentRequest) -> OrderIntentResponse:
    return OrderIntentResponse(
        order_id=f"draft-order-{payload.user_id}",
        status="pending_chatbot_backend",
        interpreted_intent=payload.text,
        missing_inputs=[
            "IC11 chatbot backend OpenAPI",
            "Order intent schema",
            "Order submission workflow",
            "Error and clarification model",
        ],
    )


def get_order_intent(order_id: str) -> OrderIntentResponse:
    return OrderIntentResponse(
        order_id=order_id,
        status="pending_chatbot_backend",
        interpreted_intent="Placeholder order intent.",
        missing_inputs=[
            "IC11 chatbot backend OpenAPI",
            "Persistent order state source",
            "Order status mapping",
        ],
    )

