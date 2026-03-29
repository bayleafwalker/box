from __future__ import annotations

import argparse
import json
from pathlib import Path

from packages.contract_kit.validation import validate_contract_examples, validate_contracts
from packages.scenario_sdk.validation import validate_scenarios


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="box-validate",
        description="Validate service contracts, scenario packs, and example payloads.",
    )
    parser.add_argument("--contracts-root", default="contracts")
    parser.add_argument("--scenarios-root", default="scenario-packs")
    parser.add_argument("--schemas-root", default="schemas")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    contracts_root = Path(args.contracts_root)
    scenarios_root = Path(args.scenarios_root)
    schemas_root = Path(args.schemas_root)

    contract_report = validate_contracts(contracts_root, schemas_root / "service-contract.schema.json")
    example_report = validate_contract_examples(contracts_root)
    scenario_report = validate_scenarios(
        scenarios_root,
        schemas_root / "scenario-pack.schema.json",
        known_services={summary.service for summary in contract_report.services},
    )

    payload = {
        "contracts": {
            "count": len(contract_report.services),
            "services": [summary.__dict__ for summary in contract_report.services],
            "issues": contract_report.issues,
        },
        "examples": {
            "count": len(example_report.examples_checked),
            "examples_checked": example_report.examples_checked,
            "issues": example_report.issues,
        },
        "scenarios": {
            "count": len(scenario_report.scenarios),
            "scenarios": scenario_report.scenarios,
            "issues": scenario_report.issues,
        },
    }

    issues = (
        contract_report.issues + example_report.issues + scenario_report.issues
    )

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(
            f"Validated {len(contract_report.services)} service contracts, "
            f"{len(scenario_report.scenarios)} scenario packs, and "
            f"{len(example_report.examples_checked)} example payloads."
        )
        if issues:
            print("Issues:")
            for issue in issues:
                print(f"- {issue}")

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
