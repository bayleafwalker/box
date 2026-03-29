# Implementation Plan

## Purpose

Turn the target architecture into a staged execution plan aligned with the repo backlog and current feature briefs.

## Current baseline

Phase 0 already exists in repo form:

- service manifests, OpenAPI contracts, and event schemas under `contracts/`
- scenario pack scaffolding under `scenario-packs/`
- validation tooling under `apps/validator/` and `packages/`
- staged requirements, feature briefs, and sprint or knowledge workflow scaffolding
- local dependency placeholders for Postgres, NATS, Talos, Terraform, and Flux

The next work is implementation, not more generic architecture invention.

## Stage 1: Kernel services

Goal:

- deliver the smallest credible business platform runtime

Scope:

- implement `party-service`, `catalog-service`, and `transaction-service`
- add service-owned Postgres schemas
- add outbox publication for emitted events
- add inbox or projection handling in `transaction-service`
- add a lightweight gateway only if it improves demo usability without hiding boundaries

Expected artifacts:

- service apps under `services/`
- migrations or schema bootstrap per service
- contract conformance tests and service-level tests
- local run path against the Compose dependency stack

Verification bar:

- create party, catalog item, and order end to end
- publish `party.created`, `catalog.item.created`, and `order.created`
- reject invalid orders without reading another service's database

## Stage 2: Scenario simulation

Goal:

- make the kernel look alive through deterministic scenario-driven activity

Scope:

- build the scenario registry and loader
- implement deterministic clock, seeded randomness, and replay support
- add simulation policies for `hotdog-stand` and `it-consultancy`
- record simulator run audit and rejection data

Expected artifacts:

- simulator runtime module
- scenario registry and loader abstractions
- policy execution loop
- simulator metrics or audit surface

Verification bar:

- one command starts a named scenario
- generated commands or events validate against the current contracts
- the operator can explain what was generated, from which seed, and why

## Stage 3: Platform and GitOps

Goal:

- make the local contract-first stack reproducible on real infrastructure

Scope:

- package services and simulator as deployable workloads
- compose CNPG, NATS, ingress, and observability in Flux
- finish the Hetzner and Talos bootstrap path
- document bootstrap, recovery, and rollback

Expected artifacts:

- Helm charts or equivalent deployment packaging
- Flux overlays under `platform/flux/`
- Terraform and Talos runnable examples under `infra/`
- operations runbooks

Verification bar:

- a fresh cluster can bootstrap from Git
- kernel services and simulator deploy without weakening their service boundaries
- rollback steps are written and executable

## Stage 4: Replacement proof

Goal:

- prove that a service can be swapped without breaking the platform

Scope:

- add contract conformance harnesses
- implement one alternate conforming service
- demonstrate routing or composition switch-over
- document rollout and rollback

Expected artifacts:

- boundary-focused compatibility tests
- alternate service implementation
- swap demo procedure and evidence

Verification bar:

- replacement candidate passes API and event compatibility checks
- gateway or routing composition switches providers without caller edits outside the boundary
- rollback is documented before the demo is considered complete

## Sequencing rules

1. Do not let infra work outrun service semantics.
2. Do not let simulator work bypass missing service implementation by writing private tables.
3. Do not add new services until a scenario demonstrates a real new boundary.
4. Do not treat monorepo imports as permission to share persistence or private models.
5. Prefer proving one coherent slice per stage over partial work across all stages at once.

## Recommended order inside Stage 1

1. `party-service`
2. `catalog-service`
3. `transaction-service`
4. gateway or entry surface

That order matches dependency shape: transactions depend on party and catalog reference facts, while the gateway depends on stable service surfaces.
