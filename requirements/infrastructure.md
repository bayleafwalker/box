# Infrastructure Requirements

## Scope

Infra and GitOps requirements for Phase 0 and Phase 3.

## Requirements

1. The infrastructure layout must preserve a separate `infra/` path for provisioning and `platform/` path for GitOps composition.
2. Hetzner/Talos/Terraform remains the preferred bootstrap path because it matches the local project ecosystem.
3. Flux remains the preferred GitOps reconciler for the initial implementation.
4. CNPG is the default stateful Postgres operator target once cluster deployment is active.
5. NATS JetStream is the default event broker for the first implementation.
6. Local development must have a lightweight dependency stack that can be inspected through Docker Compose before cluster deployment exists.
7. Recovery and rollback paths must remain Git- and version-oriented from the start.
