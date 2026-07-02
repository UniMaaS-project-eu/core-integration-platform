from app.schemas.knowledge_graph import CentralKgResponse, SPARQLQuery
from app.services.configuration import configured
from app.settings import Settings


def _source_status(settings: Settings) -> str:
    if configured(settings.ic3_knowledge_graph_base_url):
        return "Central KG base URL is configured. Response schemas are still unspecified in the supplied OpenAPI."
    return "Central KG route skeleton only. Configure IC3_KNOWLEDGE_GRAPH_BASE_URL and auth before proxying."


def get_all_classes(settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(source_status=_source_status(settings), data=[])


def get_instances(class_uri: str, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"class_uri": class_uri, "instances": []},
    )


def get_properties_for_class(class_uri: str, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"class_uri": class_uri, "properties": []},
    )


def get_properties_for_instance(instance_uri: str, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"instance_uri": instance_uri, "properties": []},
    )


def get_instances_with_property(class_uri: str, property_uri: str, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"class_uri": class_uri, "property_uri": property_uri, "instances": []},
    )


def get_instances_with_property_value(
    class_uri: str,
    property_uri: str,
    value: str,
    settings: Settings,
) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"class_uri": class_uri, "property_uri": property_uri, "value": value, "instances": []},
    )


def run_raw_sparql(payload: SPARQLQuery, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"query": payload.query, "rows": []},
    )


def get_msc_stage(product_uri: str, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"product_uri": product_uri, "stage": None},
    )


def get_msc_all_stages(product_uri: str, settings: Settings) -> CentralKgResponse:
    return CentralKgResponse(
        source_status=_source_status(settings),
        data={"product_uri": product_uri, "stages": []},
    )
