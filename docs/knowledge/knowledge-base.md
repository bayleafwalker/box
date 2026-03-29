# Knowledge Base — box
Generated: 2026-03-29T13:39:24Z

## Decisions

### Use service-owned Postgres with outbox or inbox integration instead of cross-service reads
Source: track: planning, sprint: 1
Tags: architecture, data, boundaries, outbox, inbox

The target architecture keeps party-service, catalog-service, and transaction-service on separate persistence boundaries. Cross-service invariants are enforced through contract-backed APIs and consumer-owned reference projections populated from events, with outbox publication on producers and idempotent inbox handling on consumers.

---

### Keep the first runtime thin: optional gateway, deterministic simulator, and scenario-pack overlays
Source: track: planning, sprint: 1
Tags: architecture, simulation, gateway, scenarios

The concrete platform shape is a small kernel of three services, an optional thin gateway, and a deterministic simulator that talks only through public service boundaries. Scenario packs remain overlay configuration for business behavior and must not become a hidden canonical domain model or a path to direct database mutation.

---

### Use repo-local sprint and knowledge DBs with committed renders
Source: track: ops, sprint: 1
Tags: workflow, sprintctl, kctl, repo-operations

Live sprint execution and knowledge extraction stay in repo-local SQLite databases under .sprintctl and .kctl. The only shared artifacts are the rendered sprint snapshots and knowledge base committed under docs/. This preserves the operational workflow while keeping Git diffs meaningful.

---

### Stage delivery as kernel, simulator, platform, then replacement proof
Source: track: planning, sprint: 1
Tags: planning, roadmap, architecture

The delivery order is fixed as kernel first, scenario simulation second, platform and GitOps third, and replacement proof fourth. Each slice proves a coherent architectural claim and avoids investing in infrastructure before there is a credible business-system surface to deploy.

---

## Lessons

### Promote architecture and workflow guidance into tracked docs instead of leaving it implicit in the README
Source: track: planning, sprint: 1
Tags: workflow, docs, agents, planning, knowledge

Architecture, agent modes, and working practices should live in first-class tracked docs rather than README-only notes. For box, durable guidance belongs in docs/architecture/, docs/agents/, and docs/runbooks/project-working-practices.md, with AGENTS.md pointing to those surfaces and sprintctl or kctl carrying the live execution history.

---

### Group backlog work by product outcomes, not tool silos
Source: track: docs, sprint: 1
Tags: planning, workflow, backlog

Backlog items should be sliced by product outcome and architectural proof point rather than by broad tool categories such as docs or infra. That makes each staged packet easier to review, execute, and hand off without losing the user-visible reason for the work.

---
