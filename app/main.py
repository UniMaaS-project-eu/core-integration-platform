from fastapi import FastAPI

from app.routers import (
    cloud_mfg_orchestrator,
    dpp_infrastructure,
    edc_connector,
    federated_catalogue,
    iam_data_governance,
    integration,
    intent_chatbot,
    knowledge_graph,
    resource_monitoring,
)


OPENAPI_TAGS = [
    {"name": "ic1-edc-connector", "description": "UniMaaS EDC Connector integration."},
    {"name": "ic3-knowledge-graph", "description": "Knowledge Graph integration."},
    {"name": "ic4-federated-catalogue", "description": "Federated Catalogue integration."},
    {"name": "ic5-resource-monitoring", "description": "Resource Monitoring Engine integration."},
    {"name": "ic6-iam-data-governance", "description": "IAM and Data Governance integration."},
    {"name": "ic7-dpp-infrastructure", "description": "DPP Infrastructure integration."},
    {"name": "ic11-intent-chatbot", "description": "Intent-Based Servitisation/Chatbot integration."},
    {"name": "ic15-cloud-mfg-orchestrator", "description": "Cloud Manufacturing Orchestrator integration."},
    {"name": "integration", "description": "Service healthcheck."},
]


def create_app() -> FastAPI:
    app = FastAPI(
        title="UniMaaS Core Integration Platform",
        version="0.1.0",
        summary="IC17 backend-for-frontend for UniMaaS frontend components.",
        description=(
            "FastAPI backend for the Core Integration Platform. "
            "Routes are grouped by downstream component so each integration point is visible in Swagger."
        ),
        openapi_tags=OPENAPI_TAGS,
    )

    app.include_router(integration.router)
    app.include_router(iam_data_governance.router)
    app.include_router(knowledge_graph.router)
    app.include_router(federated_catalogue.router)
    app.include_router(edc_connector.router)
    app.include_router(intent_chatbot.router)
    app.include_router(cloud_mfg_orchestrator.router)
    app.include_router(resource_monitoring.router)
    app.include_router(dpp_infrastructure.router)

    return app


app = create_app()
