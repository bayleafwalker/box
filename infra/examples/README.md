# Local Dependency Stack

The initial local stack is intentionally small:

- Postgres for service-owned persistence
- NATS with JetStream enabled for contract-driven events

This is enough to develop contract validation, service bootstraps, and simulator integration before the Hetzner/Talos/Flux path is fully wired.
