from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class ScenarioValidationReport:
    scenarios: list[str]
    issues: list[str]


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _relative(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


def validate_scenarios(
    scenarios_root: Path,
    schema_path: Path,
    known_services: set[str],
) -> ScenarioValidationReport:
    issues: list[str] = []
    scenarios: list[str] = []

    schema = _load_yaml(schema_path)
    validator = Draft202012Validator(schema)

    for scenario_path in sorted(scenarios_root.glob("*/scenario.yaml")):
        scenario = _load_yaml(scenario_path)

        if not isinstance(scenario, dict):
            issues.append(f"{_relative(scenario_path)}: scenario file must be a mapping.")
            continue

        for error in validator.iter_errors(scenario):
            issues.append(f"{_relative(scenario_path)}: {error.message}")

        scenario_name = str(scenario.get("scenario", scenario_path.parent.name))
        if scenario_name != scenario_path.parent.name:
            issues.append(
                f"{_relative(scenario_path)}: scenario name should match directory '{scenario_path.parent.name}'."
            )

        services_enabled = set(scenario.get("services_enabled", []))
        unknown_services = sorted(services_enabled - known_services)
        if unknown_services:
            issues.append(
                f"{_relative(scenario_path)}: unknown services referenced: {', '.join(unknown_services)}."
            )

        if "transaction-service" in services_enabled and not {
            "party-service",
            "catalog-service",
        }.issubset(services_enabled):
            issues.append(
                f"{_relative(scenario_path)}: transaction-service requires party-service and catalog-service."
            )

        payment_mix = scenario.get("simulation", {}).get("payment_mix")
        if isinstance(payment_mix, dict):
            total = sum(float(value) for value in payment_mix.values())
            if abs(total - 1.0) > 0.001:
                issues.append(
                    f"{_relative(scenario_path)}: simulation.payment_mix must sum to 1.0."
                )

        scenarios.append(scenario_name)

    return ScenarioValidationReport(scenarios=scenarios, issues=issues)
