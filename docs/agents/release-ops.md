# Release And Ops Mode

## Purpose

Prepare work for repeatable local verification, CI, and deployment-oriented handoff.

Use `../runbooks/project-working-practices.md` for the release loop and `../runbooks/sprint-and-knowledge-operations.md` for sprint or knowledge state updates tied to release work.

## Required inputs

- the local verification targets and expected outcomes
- the deployment surfaces touched by the change
- the environment assumptions for Postgres, NATS, Docker Compose, Helm, or Flux paths involved

## Required verification

- run the smallest useful checks first and `make verify-fast` before pushing substantial changes
- keep deployment and workflow docs aligned with runtime changes
- verify local Compose, validation, test, and packaging paths when they are affected
- note clearly which checks were run and which were not possible

## Stop and escalate

- stop if deployment guidance would publish an unverified change
- stop if runtime assumptions depend on secrets or infrastructure not represented in repo docs
