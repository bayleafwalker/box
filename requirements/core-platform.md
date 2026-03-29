# Core Platform Requirements

## Scope

Phase 0 and Phase 1 platform kernel requirements.

## Requirements

1. The platform must define explicit contracts for `party-service`, `catalog-service`, and `transaction-service`.
2. Each service must own its persistence boundary; no direct cross-service reads or writes are allowed.
3. Synchronous behavior must be described through OpenAPI.
4. Event behavior must be described through JSON Schema.
5. Contract manifests must declare emitted events, consumed events, and invariants.
6. Service implementation may live in a monorepo, but compatibility must be enforced through contracts rather than import-level coupling.
7. Replacement of one service with another conforming implementation must be treated as a first-class future proof point.
