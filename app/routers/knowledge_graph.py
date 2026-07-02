from fastapi import APIRouter, Query

from app.schemas.knowledge_graph import CentralKgResponse, SPARQLQuery
from app.services import knowledge_graph_service
from app.settings import get_settings

router = APIRouter(prefix="/knowledge-graph", tags=["ic3-knowledge-graph"])


@router.get("", response_model=CentralKgResponse)
def read_root() -> CentralKgResponse:
    return CentralKgResponse(source_status="Central KG integration endpoint group.")


@router.get("/classes", response_model=CentralKgResponse)
def get_all_classes() -> CentralKgResponse:
    return knowledge_graph_service.get_all_classes(settings=get_settings())


@router.get("/instances", response_model=CentralKgResponse)
def get_instances(class_uri: str = Query(..., description="Class URI to retrieve instances for.")) -> CentralKgResponse:
    return knowledge_graph_service.get_instances(class_uri=class_uri, settings=get_settings())


@router.get("/properties", response_model=CentralKgResponse)
def get_properties_for_class(
    class_uri: str = Query(..., description="Class URI to retrieve properties for."),
) -> CentralKgResponse:
    return knowledge_graph_service.get_properties_for_class(class_uri=class_uri, settings=get_settings())


@router.get("/instance", response_model=CentralKgResponse)
def get_properties_for_instance(
    instance_uri: str = Query(..., description="Instance URI to retrieve properties for."),
) -> CentralKgResponse:
    return knowledge_graph_service.get_properties_for_instance(instance_uri=instance_uri, settings=get_settings())


@router.get("/instances/by-property", response_model=CentralKgResponse)
def get_instances_with_property(
    class_uri: str = Query(..., description="Class URI to filter instances by."),
    property_uri: str = Query(..., description="Property URI that instances must contain."),
) -> CentralKgResponse:
    return knowledge_graph_service.get_instances_with_property(
        class_uri=class_uri,
        property_uri=property_uri,
        settings=get_settings(),
    )


@router.get("/instances/by-property-value", response_model=CentralKgResponse)
def get_instances_with_property_value(
    class_uri: str = Query(..., description="Class URI to filter instances by."),
    property_uri: str = Query(..., description="Property URI that must match the value."),
    value: str = Query(..., description="Property value to match."),
) -> CentralKgResponse:
    return knowledge_graph_service.get_instances_with_property_value(
        class_uri=class_uri,
        property_uri=property_uri,
        value=value,
        settings=get_settings(),
    )


@router.post("/sparql", response_model=CentralKgResponse)
def run_raw_sparql(payload: SPARQLQuery) -> CentralKgResponse:
    return knowledge_graph_service.run_raw_sparql(payload, settings=get_settings())


@router.get("/msc/get_stage", response_model=CentralKgResponse)
def get_msc_stage(product_uri: str = Query(..., description="Product URI to retrieve the MSC stage for.")) -> CentralKgResponse:
    return knowledge_graph_service.get_msc_stage(product_uri=product_uri, settings=get_settings())


@router.get("/msc/get_all_stages", response_model=CentralKgResponse)
def get_msc_all_stages(
    product_uri: str = Query(..., description="Product URI to retrieve all MSC stages for."),
) -> CentralKgResponse:
    return knowledge_graph_service.get_msc_all_stages(product_uri=product_uri, settings=get_settings())
