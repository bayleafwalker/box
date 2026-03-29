# ADR 0001: Contract-First Platform Kernel

## Status

Accepted

## Context

The project goal is to build a small but credible "business in a box" platform:

- provisionable on demand
- deployable through GitOps
- modular at the service boundary
- able to simulate realistic business activity through scenario packs

The main technical failure modes are already clear:

- shared-database coupling between services
- scenario logic that bypasses business interfaces
- infra work outrunning service semantics
- over-modeling "all businesses" into a canonical swamp

The repository therefore needs a hard initial boundary that can survive later implementation pressure.

## Decision

Adopt a contract-first kernel with these rules:

1. The first service set is fixed to `party-service`, `catalog-service`, and `transaction-service`.
2. Every service owns its own persistence and exposes behavior only through explicit API and event contracts.
3. Contracts are declared under `contracts/<service>/` and versioned independently per service manifest.
4. Scenario packs are overlays, not canonical enterprise models. They enable services, map entity categories, provide seed data, and define simulation policies.
5. The simulator must validate its emitted payloads against the same contracts consumed by services.
6. Terraform/Talos/Flux layout is separated from application and scenario code so infra evolution does not blur service boundaries.

## Consequences

Positive:

- service replacement demos stay credible because compatibility is anchored in declared contracts
- scenario packs can vary business semantics without rewriting platform primitives
- local validation becomes possible before full service implementation exists
- infra work can proceed in parallel with contract and simulator work

Negative:

- early implementation feels slower because contracts and docs are written first
- some cross-service convenience shortcuts are intentionally disallowed
- the first few local demos will use stubs and examples rather than full runtime behavior

## Non-goals for Phase 0

- multi-tenant isolation
- billing and ledger depth
- generalized canonical model for every industry
- direct simulator writes into service databases

## Follow-up

- add contract compatibility checks between versions
- implement reference FastAPI services that conform to the current contracts
- add a simulator engine that emits contract-valid events only
