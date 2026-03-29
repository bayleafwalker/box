# Sprint And Knowledge Operations

## Purpose

This repository uses `sprintctl` for live sprint state and `kctl` for durable knowledge capture.

The local SQLite databases are operational state. The committed render outputs are the shared repo view.

## Local-only state

- `.sprintctl/sprintctl.db`
- `.kctl/kctl.db`
- `sprint-*.json`
- `handoff-*.json`

## Committed shared artifacts

- `docs/sprint-snapshots/sprint-current.txt`
- `docs/sprint-snapshots/backlog-master.txt`
- `docs/knowledge/knowledge-base.md`

## Operating rules

1. Load `.envrc` before using either CLI.
2. Treat live `sprintctl` state as the source of truth for current work status and claims.
3. Refresh sprint snapshots only after the live DB state is correct.
4. Record durable decisions and lessons as structured `sprintctl event` entries.
5. Run `kctl extract`, review candidates, and publish knowledge intentionally rather than as part of unrelated edits.

## Useful commands

```bash
make sprint-snapshot
make sprint-backlog-snapshot
make sprint-check
kctl extract
kctl review list --json
make kctl-render
```
