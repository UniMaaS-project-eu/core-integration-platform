from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_openapi_contains_frontend_tags() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    tag_names = {tag["name"] for tag in response.json()["tags"]}
    assert {
        "dashboard",
        "registration",
        "search",
        "provider-assets",
        "chatbot-orders",
        "order-status",
        "infrastructure-status",
        "dpp",
    }.issubset(tag_names)


def test_healthcheck_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_blocked_infrastructure_route_returns_named_missing_inputs() -> None:
    response = client.get("/infrastructure-status/assets")
    assert response.status_code == 501
    detail = response.json()["detail"]
    assert detail["component"] == "IC5 Resource Monitoring Engine"
    assert "API spec" in detail["missing_inputs"]


def test_designable_order_status_route_returns_workflow_shape() -> None:
    response = client.get("/order-status/workflows?order_id=order-123")
    assert response.status_code == 200
    payload = response.json()
    assert payload["workflows"][0]["order_id"] == "order-123"
    assert payload["workflows"][0]["source_component"] == "IC15 Cloud Mfg Orchestrator"
