from typing import Annotated, Literal

from pydantic import BaseModel, Field


RdfSerialization = Literal["TTL", "RDF/XML", "JSON-LD"]


class RdfAssetProperties(BaseModel):
    name: str = Field(..., examples=["RDFService Example Dataset"])
    description: str = Field(..., examples=["Dataset for the RDF service for testing"])
    related_spatial_region: str | None = Field(default=None, examples=["Belgium"])


class SparqlEndpointRdfService(BaseModel):
    service_type: Literal["sparqlendpoint"] = "sparqlendpoint"
    sparql_endpoint: str = Field(..., examples=["http://localhost:3030/provider/sparql"])
    sparql_query: str = Field(
        ...,
        examples=[
            "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
            "CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }"
        ],
    )
    username: str | None = None
    password: str | None = None


class HttpEndpointRdfService(BaseModel):
    service_type: Literal["httpendpoint"] = "httpendpoint"
    http_endpoint: str = Field(..., examples=["https://provider.example.org/datasets/service.ttl"])
    serialization: RdfSerialization = "TTL"
    encoding: str = "UTF-8"


class FileRdfService(BaseModel):
    service_type: Literal["file"] = "file"
    file_path: str = Field(..., examples=["/data/provider/service.ttl"])
    serialization: RdfSerialization = "TTL"
    encoding: str = "UTF-8"


RdfServiceDataAddress = Annotated[
    SparqlEndpointRdfService | HttpEndpointRdfService | FileRdfService,
    Field(discriminator="service_type"),
]


class RdfServiceAssetRegistrationRequest(BaseModel):
    asset_id: str = Field(..., examples=["request-rdf-service"])
    properties: RdfAssetProperties
    data_address: RdfServiceDataAddress


class AssetRegistrationResponse(BaseModel):
    asset_id: str
    status: Literal["drafted", "pending_edc_deployment"]
    edc_data_address_type: Literal["RDFService"] = "RDFService"
    service_type: Literal["sparqlendpoint", "httpendpoint", "file"]
    required_backend: str
    missing_inputs: list[str]


class RdfSinkFileDestination(BaseModel):
    store: Literal["file"] = "file"
    target_url: str = Field(..., examples=["/path/to/output/directory"])
    file_name: str | None = Field(default=None, examples=["dataset.ttl"])
    serialization: RdfSerialization = "TTL"


class RdfSinkSparqlDestination(BaseModel):
    store: Literal["sparql"] = "sparql"
    target_url: str = Field(..., examples=["http://localhost:3030/consumer/sparql"])
    graph: str | None = Field(default=None, examples=["default"])
    username: str | None = None
    password: str | None = None


RdfSinkDestination = Annotated[
    RdfSinkFileDestination | RdfSinkSparqlDestination,
    Field(discriminator="store"),
]


class RdfSinkPushTransferRequest(BaseModel):
    asset_id: str = Field(..., examples=["request-rdf-service"])
    counter_party_address: str = Field(..., examples=["https://provider.example.org/api/dsp"])
    connector_id: str = Field(..., examples=["provider-connector"])
    contract_id: str = Field(..., examples=["contract-agreement-id"])
    data_destination: RdfSinkDestination
    protocol: Literal["dataspace-protocol-http"] = "dataspace-protocol-http"
    transfer_type: Literal["RDFSink-PUSH"] = "RDFSink-PUSH"


class HttpProxyPullTransferRequest(BaseModel):
    asset_id: str = Field(..., examples=["request-rdf-service"])
    counter_party_address: str = Field(..., examples=["https://provider.example.org/api/dsp"])
    connector_id: str = Field(..., examples=["provider-connector"])
    contract_id: str = Field(..., examples=["contract-agreement-id"])
    protocol: Literal["dataspace-protocol-http"] = "dataspace-protocol-http"
    transfer_type: Literal["HttpData-PULL"] = "HttpData-PULL"
    requested_serialization: RdfSerialization | None = Field(default=None, examples=["RDF/XML"])


RdfTransferRequest = Annotated[
    RdfSinkPushTransferRequest | HttpProxyPullTransferRequest,
    Field(discriminator="transfer_type"),
]


class RdfTransferResponse(BaseModel):
    asset_id: str
    status: Literal["drafted", "pending_edc_deployment"]
    transfer_type: Literal["RDFSink-PUSH", "HttpData-PULL"]
    required_backend: str
    missing_inputs: list[str]

