# Core Integration Platform Integration Tracking

This file tracks IC17 interfaces, current design status, and missing inputs.

## Integration Landscape

```mermaid
flowchart LR
  FE["CEL Frontend Components<br/>IC18-IC25"] --> IC17["Core Integration Platform<br/>FastAPI BFF + Swagger"]

  IC17 --> EDC["IC1 UniMaaS EDC Connector<br/>partial spec"]
  IC17 --> KG["IC3 Knowledge Graph<br/>SPARQL partial spec"]
  IC17 --> FC["IC4 Federated Catalogue<br/>partial spec"]
  IC17 --> RME["IC5 Resource Monitoring Engine<br/>missing spec"]
  IC17 --> IAM["IC6 IAM & Data Governance<br/>under definition"]
  IC17 --> DPP["IC7 DPP Infrastructure<br/>NGSI-LD partial spec"]
  IC17 --> ARGO["IC15 Cloud Mfg Orchestrator<br/>Argo/K8s workflow status"]

  classDef ready fill:#d9f7e8,stroke:#1b7f4c,color:#0f3d2a;
  classDef partial fill:#fff4cc,stroke:#a06a00,color:#4d3300;
  classDef blocked fill:#ffe0e0,stroke:#a33,color:#5c1111;

  class ARGO ready;
  class EDC,KG,FC,IAM,DPP partial;
  class RME blocked;
```





## Status Matrix


| Component                      | Partner | Frontend capability                                                                      | Backend dependency                                                 | Known spec/reference                                                                                                                  | Readiness                    | Blocking questions                                                                                 | Owner       | Next update date |
| ------------------------------ | ------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------- | ----------- | ---------------- |
| IC1 UniMaaS EDC Connector      | FLM     | Dataset registration and transfer initiation from search/provider flows                  | EDC management/catalogue/transfer APIs with UniMaaS RDF extensions | EDC standard API and `UniMaaS-project-eu/edc-rdf` RDFService/RDFSink examples                                                         | Partially designable         | Final deployed API URL, auth mechanism, exact EDC version, supported endpoints, error model        | FLM + NET   | TBD              |
| IC3 Knowledge Graph            | FLM     | Customer search and semantic query support                                               | SPARQL endpoint or REST API aligned to MSC ontology                | `UniMaaS-project-eu/MSC-Ontology-RDF`; API/details still TBD in D7.1                                                                  | Partially designable         | Final query shapes, accepted parameters, result format, pagination, auth/access rules              | FLM + NET   | TBD              |
| IC4 Federated Catalogue        | FLM     | Catalogue search/read for customer search                                                | EDC federated catalogue management API                             | EDC federated catalogue management API; UniMaaS-specific API still TBD                                                                | Partially designable         | UniMaaS catalogue response schema, filters, pagination, auth, sample payloads                      | FLM + NET   | TBD              |
| IC5 Resource Monitoring Engine | NTUA    | Infrastructure status and monitoring views                                               | Resource Monitoring Engine REST API                                | D7.1 marks specification as TBD                                                                                                       | Blocked                      | API spec, data model, polling vs streaming, asset identifiers, auth                                | NTUA + NET  | TBD              |
| IC6 IAM & Data Governance      | ODINS   | Registration, identity validation, role assignment, authorization checks                 | IAM and governance REST APIs                                       | Expected schemas: registration request, identity profile, role assignment, credential status, authorization response, policy metadata | Partially blocked            | Final OpenAPI, realm/domain model, provider/consumer role model, token flow, policy metadata shape | ODINS + NET | TBD              |
| IC7 DPP Infrastructure         | ODINS   | DPP product lifecycle read/manage views                                                  | DPP REST API backed by NGSI-LD entities managed through Orion-LD   | NGSI-LD/Orion-LD direction known; final DPP API pending                                                                               | Partially designable         | Final DPP entity schemas, identifiers, allowed writes, auth, error model                           | ODINS + NET | TBD              |
| IC15 Cloud Mfg Orchestrator    | NTUA    | Order and workflow status views                                                          | Argo Workflows/Kubernetes workflow state                           | Kubernetes CRD schema followed by Argo Workflows                                                                                      | Designable first             | Cluster URL/access, namespaces, auth token flow, selected status fields, refresh expectations      | NTUA + NET  | TBD              |
| IC18-IC25 CEL UI components    | CEL     | Dashboard, registration, search, provider UI, chatbot, order status, infrastructure, DPP | IC17 OpenAPI generated by FastAPI                                  | This repository's FastAPI `/docs` and `/openapi.json`                                                                                 | Designable from IC17 outward | Confirm route names, frontend DTO preferences, UI-specific aggregation needs                       | CEL + NET   | TBD              |

