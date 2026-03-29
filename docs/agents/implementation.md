# Implementation Mode

## Purpose

Execute an approved plan while preserving contract-first boundaries and keeping verification close to the change.

Use `../runbooks/project-working-practices.md` for startup order, done criteria, and close-out expectations.

## Required inputs

- an approved plan or a request with clear local intent
- live sprint item and claim state when the work is sprint-scoped
- the relevant contracts, scenario packs, and architecture docs
- the local verification targets that must pass before close-out

## Required verification

- keep each service inside its own persistence boundary
- update tests with behavior changes
- update contracts, scenario packs, docs, and requirements together when the public surface changes
- keep simulator logic on public boundaries only
- refresh sprint state and snapshots when the work is tracked in `sprintctl`

## Stop and escalate

- stop if a needed design choice is not decided by user instruction or repo docs
- stop if the change would bypass service contracts for convenience
- stop if a necessary edit conflicts with unexpected user changes
