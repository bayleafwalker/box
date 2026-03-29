# Planning Mode

## Purpose

Turn a request into a concrete implementation or documentation plan before edits begin.

Use `../runbooks/project-working-practices.md` to decide whether the task should start as new scope registration, sprint resumption, docs work, or direct implementation.

## Required inputs

- the user goal and success criteria
- current repo state from direct inspection
- live `sprintctl` state when the work is sprint-scoped
- the affected contracts, requirements, or architecture docs

## Required verification

- confirm the service and data boundaries first
- confirm whether the work already exists in `sprintctl`
- confirm whether any exclusive claim belongs to the current live identity before planning implementation under that item
- identify the verification path that will prove the outcome
- identify which docs need updates along with the code or workflow change

## Stop and escalate

- stop if the plan depends on shared-database shortcuts
- stop if the request needs a new service boundary that has not been justified by a scenario
- stop if a sprint-scoped item is exclusively claimed and ownership cannot be proven
