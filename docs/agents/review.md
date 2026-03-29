# Review Mode

## Purpose

Review changes with a bias toward bugs, contract drift, architectural regressions, and missing tests.

Use `../runbooks/project-working-practices.md` for review expectations and done criteria by change class.

## Required inputs

- the diff or touched files
- the relevant requirements, contracts, and architecture docs
- the tests or verification paths that should cover the change

## Required verification

- findings before summary
- check for hidden cross-service data coupling
- check that behavior changes updated tests
- check that contract changes updated related docs and scenario packs
- call out residual risk explicitly if a replacement-proof or simulator boundary is still unverified

## Stop and escalate

- stop if the review cannot be completed accurately without missing files or generated artifacts
- stop if the change introduces a new architectural rule without docs support
