# Agent Guides

## Purpose

This directory holds repo-specific guidance for planning, implementation, review, and release-oriented work.

Start here after `README.md` when the task needs process guidance in addition to code or architecture context.

## Reading order

1. `../runbooks/project-working-practices.md`
2. `../architecture/platform-architecture.md`
3. the mode guide that matches the task:
   - `planning.md`
   - `implementation.md`
   - `review.md`
   - `release-ops.md`

## Tool and skill selection

Prefer repo-local context and tools first:

- `rg` and direct file reads for discovery
- `sprintctl` and `kctl` for live execution and durable knowledge state
- `make validate`, `make test`, and `make verify-fast` for verification

If the runtime exposes reusable skills or plugins, use the smallest matching one:

- GitHub triage or review-comment skills for PR, issue, and CI work
- OpenAI docs skills only for OpenAI product or API questions
- plugin or skill creation helpers only when the task is explicitly about Codex extensions

Do not let generic workflow skills replace reading the repo's contracts, architecture docs, or runbooks.
