from typing import Any

from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    id: str
    title: str
    description: str
    source_component: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]
    sources: list[str]
    source_status: str


class SparqlQueryRequest(BaseModel):
    query: str = Field(..., description="SPARQL query aligned to the MSC ontology.")


class SparqlQueryResponse(BaseModel):
    source_component: str
    accepted: bool
    source_status: str
    rows: list[dict[str, Any]]

