from fastapi import APIRouter, Query

from app.schemas.search import SearchResponse, SparqlQueryRequest, SparqlQueryResponse
from app.services import search_service
from app.settings import get_settings

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/services", response_model=SearchResponse)
def search_services(
    query: str = Query(..., description="User-facing search text."),
    limit: int = Query(10, ge=1, le=100),
) -> SearchResponse:
    return search_service.search_services(query=query, limit=limit, settings=get_settings())


@router.post("/sparql", response_model=SparqlQueryResponse)
def sparql_query(payload: SparqlQueryRequest) -> SparqlQueryResponse:
    return search_service.sparql_query(payload, settings=get_settings())

