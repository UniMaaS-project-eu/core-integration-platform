from fastapi import APIRouter, Query

from app.schemas.knowledge_graph import SearchResponse, SparqlQueryRequest, SparqlQueryResponse
from app.services import knowledge_graph_service
from app.settings import get_settings

router = APIRouter(prefix="/search", tags=["ic3-knowledge-graph", "ic4-federated-catalogue"])


@router.get("/services", response_model=SearchResponse)
def search_catalogue(
    query: str = Query(..., description="User-facing search text."),
    limit: int = Query(10, ge=1, le=100),
) -> SearchResponse:
    return knowledge_graph_service.search_catalogue(query=query, limit=limit, settings=get_settings())


@router.post("/sparql", response_model=SparqlQueryResponse)
def sparql_query(payload: SparqlQueryRequest) -> SparqlQueryResponse:
    return knowledge_graph_service.sparql_query(payload, settings=get_settings())
