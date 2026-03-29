# Documentation

- `architecture/` expands the contract-first ADR into target platform, data, and implementation guidance.
- `agents/` contains repo-specific mode guides and tool or skill-selection notes for AI-assisted work.
- `adr/0001-contract-first-platform.md` defines the core architectural constraints.
- `features/` contains the baseline delivery slices used for backlog staging.
- `knowledge/knowledge-base.md` is the committed knowledge render published from `kctl`.
- `product/vision.md` states the product framing and phased delivery target.
- `runbooks/project-working-practices.md` defines the default working loops and done criteria for this repo.
- `runbooks/sprint-and-knowledge-operations.md` defines the local workflow for sprint and knowledge state.
- `scenarios/README.md` describes how scenario packs fit into the system.
- `sprint-snapshots/` contains committed sprint renders from `sprintctl`.

The root principle for this repository is simple: infra, services, and simulators all compose through explicit contracts instead of through undocumented shared state.
