SHELL := /usr/bin/bash

PYTHON := $(shell if [ -x .venv/bin/python ]; then echo .venv/bin/python; else command -v python; fi)
PYTEST := $(PYTHON) -m pytest
RUFF := $(PYTHON) -m ruff
MYPY := $(PYTHON) -m mypy
BACKLOG_SPRINT_ID ?= 2
STATE_ENV := source .envrc &&

.PHONY: lint typecheck test validate compose-config verify-fast \
	sprint-snapshot sprint-backlog-snapshot sprint-check \
	kctl-status kctl-render

lint:
	$(RUFF) check .

typecheck:
	$(MYPY) apps packages tests

test:
	$(PYTEST) -q

validate:
	$(PYTHON) -m apps.validator.main

compose-config:
	docker compose -f infra/examples/compose.yaml config >/dev/null

sprint-snapshot:
	mkdir -p docs/sprint-snapshots
	$(STATE_ENV) sprintctl render > docs/sprint-snapshots/sprint-current.txt

sprint-backlog-snapshot:
	mkdir -p docs/sprint-snapshots
	$(STATE_ENV) sprintctl render --sprint-id $(BACKLOG_SPRINT_ID) > docs/sprint-snapshots/backlog-master.txt

sprint-check:
	$(STATE_ENV) sprintctl maintain check

kctl-status:
	$(STATE_ENV) kctl status --json

kctl-render:
	mkdir -p docs/knowledge
	$(STATE_ENV) kctl render --output docs/knowledge/knowledge-base.md

verify-fast: lint typecheck test validate compose-config
