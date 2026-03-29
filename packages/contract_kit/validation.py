from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class ContractSummary:
    service: str
    version: str
    api_count: int
    emitted_event_count: int
    consumed_event_count: int


@dataclass(frozen=True)
class ContractValidationReport:
    services: list[ContractSummary]
    issues: list[str]


@dataclass(frozen=True)
class ContractExampleReport:
    examples_checked: list[str]
    issues: list[str]


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _relative(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


def _validate_openapi_document(path: Path, service_name: str) -> list[str]:
    issues: list[str] = []
    document = _load_yaml(path)

    if not isinstance(document, dict):
        return [f"{_relative(path)}: OpenAPI document must be a mapping."]

    if "openapi" not in document:
        issues.append(f"{_relative(path)}: missing required 'openapi' field.")
    if not isinstance(document.get("paths"), dict) or not document.get("paths"):
        issues.append(f"{_relative(path)}: must declare at least one API path.")

    info = document.get("info")
    if not isinstance(info, dict):
        issues.append(f"{_relative(path)}: missing required 'info' mapping.")
    else:
        if not info.get("title"):
            issues.append(f"{_relative(path)}: missing info.title.")
        if not info.get("version"):
            issues.append(f"{_relative(path)}: missing info.version.")
        if service_name not in str(info.get("title", "")):
            issues.append(
                f"{_relative(path)}: info.title should identify {service_name}."
            )

    return issues


def _validate_event_schema(path: Path) -> list[str]:
    issues: list[str] = []
    schema = _load_json(path)

    if not isinstance(schema, dict):
        return [f"{_relative(path)}: event schema must be a JSON object."]
    if "$schema" not in schema:
        issues.append(f"{_relative(path)}: missing JSON Schema '$schema'.")
    if schema.get("type") != "object":
        issues.append(f"{_relative(path)}: root schema type must be 'object'.")

    Draft202012Validator.check_schema(schema)
    return issues


def validate_contracts(contracts_root: Path, schema_path: Path) -> ContractValidationReport:
    issues: list[str] = []
    summaries: list[ContractSummary] = []

    manifest_schema = _load_json(schema_path)
    manifest_validator = Draft202012Validator(manifest_schema)

    for manifest_path in sorted(contracts_root.glob("*/service.yaml")):
        manifest = _load_yaml(manifest_path)

        if not isinstance(manifest, dict):
            issues.append(f"{_relative(manifest_path)}: service manifest must be a mapping.")
            continue

        for error in manifest_validator.iter_errors(manifest):
            issues.append(f"{_relative(manifest_path)}: {error.message}")

        service_name = str(manifest.get("service", manifest_path.parent.name))
        service_dir = manifest_path.parent

        for api in manifest.get("apis", []):
            openapi_path = Path(str(api["openapi"]))
            if not openapi_path.exists():
                issues.append(f"{_relative(manifest_path)}: missing API contract {openapi_path}.")
                continue
            issues.extend(_validate_openapi_document(openapi_path, service_name))

        for event_group in ("events_emitted", "events_consumed"):
            for event in manifest.get(event_group, []):
                schema_file = Path(str(event["schema"]))
                if not schema_file.exists():
                    issues.append(
                        f"{_relative(manifest_path)}: missing event schema {schema_file}."
                    )
                    continue
                try:
                    issues.extend(_validate_event_schema(schema_file))
                except Exception as exc:  # pragma: no cover - defensive path
                    issues.append(f"{_relative(schema_file)}: failed to validate schema: {exc}")

        if service_dir.name != service_name:
            issues.append(
                f"{_relative(manifest_path)}: service name should match directory '{service_dir.name}'."
            )

        summaries.append(
            ContractSummary(
                service=service_name,
                version=str(manifest.get("version", "")),
                api_count=len(manifest.get("apis", [])),
                emitted_event_count=len(manifest.get("events_emitted", [])),
                consumed_event_count=len(manifest.get("events_consumed", [])),
            )
        )

    return ContractValidationReport(services=summaries, issues=issues)


def validate_contract_examples(contracts_root: Path) -> ContractExampleReport:
    issues: list[str] = []
    checked: list[str] = []

    for schema_path in sorted(contracts_root.glob("*/events/*.schema.json")):
        example_name = schema_path.name.replace(".schema.json", ".json")
        example_path = schema_path.parent.parent / "examples" / example_name
        if not example_path.exists():
            issues.append(f"{_relative(schema_path)}: missing paired example {example_path}.")
            continue

        schema = _load_json(schema_path)
        example = _load_json(example_path)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(example), key=lambda error: error.path)
        if errors:
            for error in errors:
                issues.append(f"{_relative(example_path)}: {error.message}")
        checked.append(_relative(example_path))

    return ContractExampleReport(examples_checked=checked, issues=issues)
