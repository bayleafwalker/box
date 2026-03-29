# Replacement Proof

## Objective

Prove that the architecture is modular by swapping a contract-conforming implementation without breaking the rest of the platform.

## User value

- the project demonstrates real service interchangeability rather than monorepo theater
- integration contracts become meaningful release artifacts
- the demo platform gains a concrete architectural proof point

## Scope

- contract conformance test harness
- at least one alternate implementation for a kernel boundary
- gateway or routing support to switch implementations
- deployment and rollback workflow for the swap demo

## Out of scope

- generic plugin marketplace work
- supporting arbitrary third-party services from day one

## First delivery bar

- one service can be swapped for an alternate implementation
- conformance tests gate the swap
- rollout and rollback are documented and repeatable
