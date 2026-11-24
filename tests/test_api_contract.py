from fastapi.testclient import TestClient

from app.main import app
from app.services import federated_catalogue_service
from app.settings import Settings


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


def test_knowledge_graph_openapi_matches_central_kg_routes() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    payload = response.json()
    paths = payload["paths"]
    schemas = payload["components"]["schemas"]
    assert "/knowledge-graph" in paths
    assert "/knowledge-graph/classes" in paths
    assert "/knowledge-graph/instances" in paths
    assert "/knowledge-graph/properties" in paths
    assert "/knowledge-graph/instance" in paths
    assert "/knowledge-graph/instances/by-property" in paths
    assert "/knowledge-graph/instances/by-property-value" in paths
    assert "/knowledge-graph/sparql" in paths
    assert "/knowledge-graph/msc/get_stage" in paths
    assert "/knowledge-graph/msc/get_all_stages" in paths
    assert "SPARQLQuery" in schemas


def test_federated_catalogue_openapi_matches_access_api_routes() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    payload = response.json()
    paths = payload["paths"]
    schemas = payload["components"]["schemas"]
    assert "/federated-catalogue" in paths
    assert "/federated-catalogue/datasets" in paths
    dataset_post = paths["/federated-catalogue/datasets"]["post"]
    assert dataset_post["tags"] == ["ic4-federated-catalogue"]
    assert "fitlers" in dataset_post["description"]
    request_body = dataset_post["requestBody"]
    assert request_body.get("required") is not True
    body_schema = request_body["content"]["application/json"]["schema"]
    assert {"$ref": "#/components/schemas/DatasetFilters"} in body_schema["anyOf"]
    assert {"type": "null"} in body_schema["anyOf"]

    filters = schemas["DatasetFilters"]
    assert set(filters["properties"]) == {"@id", "dcat:dataset", "dspace:participantId"}
    assert filters["properties"]["dcat:dataset"]["items"]["type"] == "string"
    assert "required" not in filters
    assert filters["additionalProperties"]["anyOf"] == [
        {"items": {}, "type": "array"},
        {"additionalProperties": True, "type": "object"},
        {"type": "string"},
    ]
    assert "FederatedCatalogueResponse" in schemas


def test_federated_catalogue_routes_return_placeholder_envelope() -> None:
    root = client.get("/federated-catalogue")
    assert root.status_code == 200
    root_body = root.json()
    assert root_body["source_component"] == "IC4 Federated Catalogue"
    assert "pending" in root_body["source_status"]
    assert root_body["data"] is None

    empty_object = client.post("/federated-catalogue/datasets", json={})
    assert empty_object.status_code == 200
    assert empty_object.json()["data"] == {"filters": {}, "datasets": []}
    assert "pending" in empty_object.json()["source_status"]

    omitted_body = client.post("/federated-catalogue/datasets")
    assert omitted_body.status_code == 200
    assert omitted_body.json()["data"]["datasets"] == []

    null_body = client.post("/federated-catalogue/datasets", json=None)
    assert null_body.status_code == 200
    assert null_body.json()["data"]["filters"] == {}

    filtered = client.post(
        "/federated-catalogue/datasets",
        json={
            "@id": ["id1"],
            "dcat:dataset": ["http://www.w3.org/ns/msc_dms#name"],
            "dspace:participantId": ["participant_id1"],
            "@context": {"dcat": "http://www.w3.org/ns/dcat#"},
            "customFlag": "include",
        },
    )
    assert filtered.status_code == 200
    assert filtered.json()["data"]["filters"]["@id"] == ["id1"]
    assert filtered.json()["data"]["filters"]["@context"]["dcat"] == "http://www.w3.org/ns/dcat#"
    assert filtered.json()["data"]["datasets"] == []

    rejected_extra = client.post("/federated-catalogue/datasets", json={"priority": 1})
    assert rejected_extra.status_code == 422

    null_field = client.post("/federated-catalogue/datasets", json={"@id": None})
    assert null_field.status_code == 422


def test_federated_catalogue_source_status_reports_configured_url_without_forwarding() -> None:
    response = federated_catalogue_service.get_datasets(
        None,
        Settings(ic4_federated_catalogue_base_url="http://catalogue.local"),
    )
    assert response.data == {"filters": {}, "datasets": []}
    assert "base URL is configured" in response.source_status
    assert "pending" in response.source_status


def test_supplied_dataset_filters_example_does_not_match_declared_property_types() -> None:
    example = client.get("/openapi.json").json()["components"]["schemas"]["DatasetFilters"]["examples"][0]
    response = client.post("/federated-catalogue/datasets", json=example)
    assert response.status_code == 422


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
