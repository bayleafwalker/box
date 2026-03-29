# Platform And GitOps

## Objective

Promote the local contract-first stack into a reproducible Hetzner/Talos/Flux deployment path without changing the service boundaries.

## User value

- the demo can be stood up on demand on real infrastructure
- environment recovery and rollback are Git-driven
- platform services become reusable across scenarios

## Scope

- Terraform bootstrap for Hetzner resources
- Talos cluster configuration
- Flux composition for platform services and application slices
- CNPG, NATS, ingress, and observability platform wiring
- runbooks for bootstrap, upgrade, and recovery

## Out of scope

- multi-cluster fleet management
- managed cloud portability beyond the current Hetzner focus
- bespoke operators before the base GitOps path is stable

## First delivery bar

- a fresh cluster can be bootstrapped from Git
- kernel services and simulator deploy through GitOps overlays
- recovery steps are documented and reversible
