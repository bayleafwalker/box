# box

Contract-first "business in a box" monorepo scaffold for provisioning a small demo platform, deploying modular business services, and generating scenario-driven synthetic business activity.

The project starts from a deliberate split:

- `infra/` provisions the cluster chassis and local dependency stack.
- `platform/` holds GitOps and environment composition.
- `contracts/` defines the service APIs and event schemas that everything else must obey.
- `scenario-packs/` configure business overlays such as `hotdog-stand` and `it-consultancy`.
- `packages/` contains shared validation and scenario tooling.

This initial scaffold mirrors the local conventions already used in neighboring repos under `/projects/dev/*`: Python + `uv`, `Makefile`-driven verification, explicit ADRs and requirements, and separate infra versus application layout.

Repo execution state is managed locally with `sprintctl` and `kctl`, then rendered into committed shared artifacts:

- `docs/sprint-snapshots/sprint-current.txt`
- `docs/sprint-snapshots/backlog-master.txt`
- `docs/knowledge/knowledge-base.md`

## Current status

Phase 0 is initialized:

- repository scaffold and agent guidance
- architecture ADR and requirement split
- repo-scoped sprintctl and kctl workflow
- staged feature baseline and backlog plan
- three initial service contracts: party, catalog, transaction
- two scenario packs: hotdog stand, IT consultancy
- local validation CLI and pytest coverage
- Terraform/Talos/GitOps placeholders aligned to the existing Hetzner/Talos/Flux setup
- Docker Compose dependency stack for local Postgres + NATS JetStream

This is intentionally not a full business platform. It is the contract and validation base that the services and simulator can grow on top of without collapsing into a shared-database monolith.

## Repository layout

```text
.
├── AGENTS.md
├── apps/
│   └── validator/
├── contracts/
│   ├── party-service/
│   ├── catalog-service/
│   └── transaction-service/
├── docs/
│   ├── agents/
│   ├── architecture/
│   ├── adr/
│   ├── features/
│   ├── knowledge/
│   ├── product/
│   ├── runbooks/
│   └── scenarios/
├── infra/
│   ├── examples/
│   ├── talos/
│   └── terraform/
├── packages/
│   ├── contract_kit/
│   └── scenario_sdk/
├── platform/
│   ├── clusters/
│   └── flux/
├── requirements/
├── scenario-packs/
│   ├── hotdog-stand/
│   └── it-consultancy/
├── schemas/
└── tests/
```

## Quick start

```bash
uv sync --dev
make verify-fast
source .envrc
```

Validate contracts and scenario packs directly:

```bash
uv run box-validate
```

Inspect the local dependency stack:

```bash
docker compose -f infra/examples/compose.yaml config
docker compose -f infra/examples/compose.yaml up -d
```

Inspect live sprint and knowledge state:

```bash
make sprint-snapshot
make kctl-status
```

## Architecture and workflow guides

- `docs/architecture/platform-architecture.md` defines the target runtime shape for the kernel, simulator, and platform layers.
- `docs/architecture/data-architecture.md` defines service-owned persistence, outbox or inbox patterns, and cross-service data rules.
- `docs/architecture/implementation-plan.md` maps the architecture into the staged build order already reflected in the backlog.
- `docs/runbooks/project-working-practices.md` defines the default working loops and done criteria.
- `docs/agents/README.md` and `docs/agents/*.md` define repo-specific planning, implementation, review, and release guidance for AI-assisted work.

## Immediate next build steps

1. Implement reference FastAPI services behind the existing contracts.
2. Add a simulation engine that emits only contract-valid commands and events.
3. Replace the placeholder Flux and Terraform stubs with a working Hetzner/Talos bootstrap path.
4. Add contract compatibility checks before service replacement demos.
