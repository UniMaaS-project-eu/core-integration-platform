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


class CentralKgResponse(BaseModel):
    source_component: str = "IC3 Knowledge Graph"
    source_status: str
    data: Any | None = None


class SPARQLQuery(BaseModel):
    query: str = Field(..., description="Raw SPARQL query accepted by the Central KG API.")
