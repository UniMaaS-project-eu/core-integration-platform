# Core Integration Platform Integration Tracking

This file tracks IC17 interfaces, current design status, and missing inputs.

## Integration Landscape

```mermaid
flowchart LR
  FE["CEL Frontend Components"] --> IC17["Core Integration Platform"]

  IC17 -- "X" --> EDC["IC1 UniMaaS EDC Connector"]
  IC17 -- "✓" --> KG["IC3 Knowledge Graph"]
  IC17 -- "X" --> FC["IC4 Federated Catalogue"]
  IC17 -- "X" --> RME["IC5 Resource Monitoring Engine"]
  IC17 -- "X" --> IAM["IC6 IAM & Data Governance"]
  IC17 -- "X" --> DPP["IC7 DPP Infrastructure"]
  IC17 -- "X" --> ARGO["IC15 Cloud Mfg Orchestrator"]
```





## Status Matrix


| Component                      | Partner | Frontend capability                                                      | Readiness | Swagger docs                                                | Notes                                                                                              |
| ------------------------------ | ------- | ------------------------------------------------------------------------ | --------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| IC1 UniMaaS EDC Connector      | FLM     | Dataset registration and transfer initiation from search/provider flows  | Not ready |                                                             |                                                                                                    |
| IC3 Knowledge Graph            | FLM     | Customer search and semantic query support                               | Partial   | [swagger](https://unimaas-project-eu.github.io/central-kg/) | Central KG routes and query parameters are known                                                   |
| IC4 Federated Catalogue        | FLM     | Catalogue search/read for customer search                                | Not ready |                                                             |                                                                                                    |
| IC5 Resource Monitoring Engine | NTUA    | Infrastructure status and monitoring views                               | Not ready |                                                             |                                                                                                    |
| IC6 IAM & Data Governance      | ODINS   | Registration, identity validation, role assignment, authorization checks | Not ready |                                                             | Expected IAM/governance schemas are known, but final OpenAPI and token flow are missing.           |
| IC7 DPP Infrastructure         | ODINS   | DPP product lifecycle read/manage views                                  | Not ready |                                                             |                                                                                                    |
| IC15 Cloud Mfg Orchestrator    | NTUA    | Order and workflow status views                                          | Partial   |                                                             | Argo/Kubernetes workflow status is only a starting assumption. Final IC15 API contract is missing. |


