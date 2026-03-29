# Foundation And Kernel

## Objective

Deliver the smallest credible business platform kernel with explicit service boundaries and an operable local development loop.

## User value

- operators can create and inspect parties, catalog items, and transactions through stable contracts
- future simulator work has a real target surface instead of mock-only placeholders
- the repo has a predictable execution model for docs, validation, sprint state, and local dependencies

## Scope

- reference implementations for `party-service`, `catalog-service`, and `transaction-service`
- service-owned persistence with Postgres
- contract validation in CI and local development
- local dependency stack with Postgres and NATS
- lightweight gateway or entry surface for kernel APIs

## Out of scope

- tenant isolation
- production auth depth
- ledger-grade accounting
- cluster-only deployment as the first runtime target

## First delivery bar

- create party, catalog item, and transaction flows end to end
- publish `party.created`, `catalog.item.created`, and `order.created`
- keep all cross-service behavior contract-mediated
