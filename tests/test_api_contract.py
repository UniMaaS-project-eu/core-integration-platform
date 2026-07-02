from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_openapi_contains_downstream_component_tags() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    tag_names = {tag["name"] for tag in response.json()["tags"]}
    assert {
        "ic1-edc-connector",
        "ic3-knowledge-graph",
        "ic4-federated-catalogue",
        "ic5-resource-monitoring",
        "ic6-iam-data-governance",
        "ic7-dpp-infrastructure",
        "ic11-intent-chatbot",
        "ic15-cloud-mfg-orchestrator",
    }.issubset(tag_names)


def test_healthcheck_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_edc_connector_openapi_contains_rdf_extension_models() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schemas = response.json()["components"]["schemas"]
    assert "RdfServiceAssetRegistrationRequest" in schemas
    assert "SparqlEndpointRdfService" in schemas
    assert "HttpEndpointRdfService" in schemas
    assert "FileRdfService" in schemas
    assert "RdfSinkPushTransferRequest" in schemas
    assert "HttpProxyPullTransferRequest" in schemas


def test_blocked_infrastructure_route_returns_named_missing_inputs() -> None:
    response = client.get("/infrastructure-status/assets")
    assert response.status_code == 501
    detail = response.json()["detail"]
    assert detail["component"] == "IC5 Resource Monitoring Engine"
    assert "API spec" in detail["missing_inputs"]


def test_cloud_mfg_orchestrator_route_returns_workflow_shape() -> None:
    response = client.get("/order-status/workflows?order_id=order-123")
    assert response.status_code == 200
    payload = response.json()
    assert payload["workflows"][0]["order_id"] == "order-123"
    assert payload["workflows"][0]["source_component"] == "IC15 Cloud Mfg Orchestrator"
