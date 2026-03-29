# Project Working Practices

## Purpose

Define the default workflow for how work starts, moves, and closes in this repository.

Use this runbook to keep process rules durable and reviewable instead of scattering them across sprint notes or one-off prompts.

For `sprintctl` and `kctl` command details, use `sprint-and-knowledge-operations.md`.

## Source-of-truth stack

When sources disagree, follow them in this order:

1. live `sprintctl` state for active work, claims, and structured execution history
2. `docs/sprint-snapshots/sprint-current.txt` for the shared sprint render
3. `AGENTS.md`, `docs/agents/`, and runbooks for operating rules
4. contracts, requirements, ADRs, and architecture docs for intended system behavior
5. ad hoc local notes or scratch files for temporary reasoning only

Interpretation rules:

- use live `sprintctl` state to choose or resume sprint work when the DB is available
- use sprint snapshots to communicate current state, not to override live state
- promote recurring process rules from scratch notes into tracked docs

## Working loops

### 1. New scope registration

Start trigger:

- accepted scope is not yet represented in `sprintctl`

Consult first:

- relevant requirements
- current architecture docs
- active sprint context

While in progress:

- load `.envrc`
- add the sprint item in `sprintctl`
- claim it before editing files when overlap is plausible
- refresh `docs/sprint-snapshots/sprint-current.txt` after the live state is right

Close-out artifacts:

- registered sprint item
- refreshed shared sprint snapshot when the work should be visible to others

### 2. Resume sprint work

Start trigger:

- the request is to continue, pick up, or execute already-scoped sprint work

Consult first:

- `sprintctl item show`
- `sprintctl claim list`
- recent events or notes on that item

While in progress:

- load `.envrc`
- inspect claim ownership before editing files
- use `claim_id + claim_token` as the only ownership proof
- move the item to `active` before implementation when appropriate
- log decisions, blockers, and lessons as structured sprint events while they happen

Close-out artifacts:

- updated item status
- claim release or handoff
- refreshed sprint snapshot after material state changes

### 3. Docs and architecture work

Start trigger:

- the change primarily updates architecture, workflows, docs, or planning artifacts

Consult first:

- the governing ADR
- current contracts and requirements
- existing runbooks and agent guides

While in progress:

- update the durable doc, not just the README
- keep architecture docs concrete enough to guide implementation
- update `docs/README.md` when adding a new durable doc category or key doc
- update `AGENTS.md` when repo operating rules change

Close-out artifacts:

- doc updates in the tracked location
- verification that new doc paths are discoverable and consistent

### 4. Implementation

Start trigger:

- a scoped item or direct request is ready for repo changes

Consult first:

- service contracts
- scenario packs
- architecture docs
- tests and validation paths

While in progress:

- preserve the contract-first split
- keep service-owned persistence boundaries intact
- update tests with behavior changes
- update contracts, scenario packs, docs, and requirements together when the public surface changes
- keep simulator logic on public boundaries only

Close-out artifacts:

- implementation plus matching tests
- updated contracts or docs where required
- verification evidence

### 5. Review

Start trigger:

- the change shape is stable enough to inspect for regressions

Consult first:

- diff or touched files
- affected requirements and architecture docs
- tests covering the changed behavior

While in progress:

- review findings before summaries
- check for contract drift and hidden shared-state shortcuts
- call out missing tests or replacement-proof gaps explicitly

Close-out artifacts:

- findings-first review summary
- residual risks or assumptions

### 6. Release or push

Start trigger:

- work is about to go to PR, push, or CI-triggering branch

Consult first:

- local verification entrypoints
- deployment or ops docs touched by the change

While in progress:

- run focused checks first, then broader checks
- run `make verify-fast` before pushing substantial changes
- update deployment or workflow docs when the runtime path changes

Close-out artifacts:

- verification summary with commands actually run
- updated operational assumptions when needed

### 7. Sprint and knowledge close-out

Start trigger:

- sprint state changed materially or reusable lessons were learned

Consult first:

- live `sprintctl` item and sprint state
- recent decision and lesson events

While in progress:

- record the live sprint state first
- refresh `docs/sprint-snapshots/sprint-current.txt`
- run `kctl extract`
- review and publish only the candidates worth keeping
- render `docs/knowledge/knowledge-base.md` intentionally

Close-out artifacts:

- accurate sprint snapshot
- published knowledge entries when appropriate

## Done criteria by change class

### Docs-only change

Minimum done criteria:

- update the durable doc in the correct path
- update `docs/README.md` when adding a new durable doc category or important entry point
- verify consistency with nearby docs and references
- do not claim behavior changed unless code or tests changed too

### Contract change

Minimum done criteria:

- update `contracts/`
- update affected `scenario-packs/`
- update relevant docs or requirements
- run `make validate`
- add or update compatibility or contract tests where needed

### Behavior change

Minimum done criteria:

- update or add tests in the same change
- update docs or requirements when the public behavior changed
- run focused local verification and at least one end-to-end path when feasible

### Architecture or workflow change

Minimum done criteria:

- update the relevant architecture, ADR, runbook, or agent docs
- explain the boundary being preserved or changed
- verify the guidance is discoverable from `README.md`, `docs/README.md`, or `AGENTS.md` when appropriate

### Sprint-state change

Minimum done criteria:

- record state in live `sprintctl` first
- refresh the committed sprint snapshot afterward
- keep ownership transfers explicit through claims and handoffs
- capture reusable decisions or lessons as sprint events

## Coordination rules

- Claim sprint work before repo edits when ownership could overlap.
- Matching branch, actor label, or worktree path is not ownership proof.
- If an exclusive claim exists and the current session cannot prove ownership, do not edit repo files under that item until a handoff happens.
- Keep claim identity strong: `runtime_session_id`, `instance_id`, `claim_id`, and `claim_token`.
- Prefer small, explicit handoffs over implicit continuation.
