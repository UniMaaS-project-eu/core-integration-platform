from app.schemas.search import SearchResponse, SearchResult, SparqlQueryRequest, SparqlQueryResponse
from app.services.configuration import configured
from app.settings import Settings


def search_services(query: str, limit: int, settings: Settings) -> SearchResponse:
    return SearchResponse(
        query=query,
        results=[
            SearchResult(
                id="catalogue-demo-001",
                title="Demo manufacturing service",
                description="Placeholder result combining the planned Federated Catalogue and Knowledge Graph search shape.",
                source_component="IC4 Federated Catalogue / IC3 Knowledge Graph",
                metadata={
                    "limit": limit,
                    "contract_status": "partial",
                    "knowledge_graph_configured": configured(settings.ic3_knowledge_graph_base_url),
                    "federated_catalogue_configured": configured(settings.ic4_federated_catalogue_base_url),
                },
            )
        ],
        sources=["IC3 Knowledge Graph", "IC4 Federated Catalogue"],
        source_status="Partial contract. Final FLM query and catalogue schemas are pending.",
    )


def sparql_query(payload: SparqlQueryRequest, settings: Settings) -> SparqlQueryResponse:
    return SparqlQueryResponse(
        source_component="IC3 Knowledge Graph",
        accepted=True,
        source_status=(
            "SPARQL backend URL is configured, but final row schema is pending."
            if configured(settings.ic3_knowledge_graph_base_url)
            else "SPARQL route skeleton only. Configure IC3_KNOWLEDGE_GRAPH_BASE_URL and provide auth/row schema."
        ),
        rows=[],
    )
