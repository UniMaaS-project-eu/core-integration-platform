from fastapi import FastAPI

from app.routers import chatbot_orders, dpp, infrastructure_status, integration, order_status, provider_assets, registration, search


OPENAPI_TAGS = [
    {"name": "dashboard", "description": "Top-level dashboard shell and aggregated platform state."},
    {"name": "registration", "description": "Provider/client onboarding, identity, role, and authorization flows."},
    {"name": "search", "description": "Customer search over catalogue, EDC assets, and semantic knowledge graph data."},
    {"name": "provider-assets", "description": "Provider-facing service and dataset publication flows."},
    {"name": "chatbot-orders", "description": "Order creation and order intent mediation for the chatbot UI."},
    {"name": "order-status", "description": "Order and workflow execution state from the Cloud Manufacturing Orchestrator."},
    {"name": "infrastructure-status", "description": "Infrastructure monitoring views backed by the Resource Monitoring Engine."},
    {"name": "dpp", "description": "Digital Product Passport product lifecycle read and manage flows."},
    {"name": "integration", "description": "Service healthcheck."},
]


def create_app() -> FastAPI:
    app = FastAPI(
        title="UniMaaS Core Integration Platform",
        version="0.1.0",
        summary="IC17 backend-for-frontend for UniMaaS frontend components.",
        description=(
            "FastAPI backend for the Core Integration Platform. "
            "Routes are grouped by frontend capability so CEL can consume one Swagger/OpenAPI surface."
        ),
        openapi_tags=OPENAPI_TAGS,
    )

    app.include_router(integration.router)
    app.include_router(registration.router)
    app.include_router(search.router)
    app.include_router(provider_assets.router)
    app.include_router(chatbot_orders.router)
    app.include_router(order_status.router)
    app.include_router(infrastructure_status.router)
    app.include_router(dpp.router)

    return app


app = create_app()
