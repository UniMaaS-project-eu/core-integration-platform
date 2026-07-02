# Core Integration Platform Integration Tracking

This file tracks IC17 interfaces, current design status, and missing inputs.

## Integration Landscape

```mermaid
flowchart LR
  FE["CEL Frontend Components"] --> IC17["Core Integration Platform"]

  IC17 -- "X" --> EDC["IC1 UniMaaS EDC Connector"]
  IC17 -- "X" --> KG["IC3 Knowledge Graph"]
  IC17 -- "✓" --> FC["IC4 Federated Catalogue"]
  IC17 -- "X" --> RME["IC5 Resource Monitoring Engine"]
  IC17 -- "X" --> IAM["IC6 IAM & Data Governance"]
  IC17 -- "X" --> DPP["IC7 DPP Infrastructure"]
  IC17 -- "✓" --> ARGO["IC15 Cloud Mfg Orchestrator"]
```





## Status Matrix


| Component                      | Partner | Frontend capability                                                                      | Readiness | Notes                                                                                 |
| ------------------------------ | ------- | ---------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------- |
| IC1 UniMaaS EDC Connector      | FLM     | Dataset registration and transfer initiation from search/provider flows                  | Partial   | RDFService and RDFSink payload shapes are known from `edc-rdf`; final URL, auth, EDC version and endpoint list are missing. |
| IC3 Knowledge Graph            | FLM     | Customer search and semantic query support                                               | Partial   | SPARQL/MSC ontology direction is known, but query shapes and response formats are missing. |
| IC4 Federated Catalogue        | FLM     | Catalogue search/read for customer search                                                | Ready     | EDC federated catalogue management API is available as the starting contract.             |
| IC5 Resource Monitoring Engine | NTUA    | Infrastructure status and monitoring views                                               | Not ready | API spec, data model and polling/streaming approach are missing.                         |
| IC6 IAM & Data Governance      | ODINS   | Registration, identity validation, role assignment, authorization checks                 | Partial   | Expected IAM/governance schemas are known, but final OpenAPI and token flow are missing. |
| IC7 DPP Infrastructure         | ODINS   | DPP product lifecycle read/manage views                                                  | Partial   | NGSI-LD/Orion-LD direction is known, but final DPP API and entity schemas are missing.   |
| IC15 Cloud Mfg Orchestrator    | NTUA    | Order and workflow status views                                                          | Ready     | Argo/Kubernetes workflow status schema is available as the starting contract.             |
| IC18-IC25 CEL UI components    | CEL     | Dashboard, registration, search, provider UI, chatbot, order status, infrastructure, DPP | Ready     | IC17 exposes the frontend-facing OpenAPI contract through FastAPI.                        |
