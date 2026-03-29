# Agent Guidance

- Preserve the contract-first split: contracts define the allowed service surface, scenario packs overlay business behavior, and implementation follows after those are stable.
- Do not add cross-service database access. Shared repo does not imply shared persistence.
- Before pushing substantial changes, run `make verify-fast`.
- Behavior changes must update tests in the same change.
- Contract changes must update the relevant files under `contracts/`, the related scenario packs under `scenario-packs/` when affected, and the relevant docs under `docs/` or `requirements/`.
- Architecture, workflow, or stack changes must update the relevant docs under `docs/architecture/`, `docs/runbooks/`, `docs/agents/`, or `docs/adr/`.
- Keep the first kernel small: `party-service`, `catalog-service`, `transaction-service`. Add new services only when a scenario genuinely needs a new boundary.
- Scenario packs are overlays, not canonical enterprise models. Keep business-specific policy in `scenario-packs/` rather than leaking it into shared service ownership.
- Simulator logic must validate against service contracts and must not bypass public service boundaries by mutating service data stores directly.
- Infra work should preserve the existing local style: Hetzner/Talos/Terraform in `infra/`, Flux/GitOps composition in `platform/`.

Mode guides: `docs/agents/planning.md`, `docs/agents/implementation.md`, `docs/agents/review.md`, `docs/agents/release-ops.md`.
Agent workflow and tool or skill selection: `docs/agents/README.md`.
Working practices: `docs/runbooks/project-working-practices.md`.

## Sprint and knowledge state

Sprint state is managed via `sprintctl` and durable repo memory via `kctl`.

- Load `.envrc` before using either CLI. The project DBs must resolve to `.sprintctl/sprintctl.db` and `.kctl/kctl.db`.
- For repo-wide startup order, source-of-truth precedence, and change-class done criteria, use `docs/runbooks/project-working-practices.md`.
- For sprint-scoped work, consult live `sprintctl` state before repo docs when choosing or resuming work.
- For existing sprint items, inspect item state and claims, then claim or activate the item before editing repo files.
- Ownership proof is always `claim_id + claim_token`; actor labels, branches, and worktrees are advisory context only.
- Use a strong live claim identity when claiming sprint work: `runtime_session_id`, `instance_id`, and the minted `claim_token`.
- Record material sprint state in `sprintctl` first and refresh `docs/sprint-snapshots/sprint-current.txt` afterward.
- Record durable decisions and lessons as `sprintctl event` entries so `kctl extract` can promote them later.
- Log reusable process corrections, coordination decisions, and lessons as structured events when they happen rather than only at sprint close.
- Render `docs/knowledge/knowledge-base.md` intentionally after reviewing and publishing `kctl` entries.
- Repo operating rules for this workflow live in `docs/runbooks/sprint-and-knowledge-operations.md` and `docs/runbooks/project-working-practices.md`.

Current verification entrypoints:

- `make validate`
- `make test`
- `make verify-fast`
