from pathlib import Path

from packages.contract_kit.validation import validate_contract_examples, validate_contracts


def test_contract_manifests_validate() -> None:
    report = validate_contracts(Path("contracts"), Path("schemas/service-contract.schema.json"))

    assert report.issues == []
    assert [summary.service for summary in report.services] == [
        "catalog-service",
        "party-service",
        "transaction-service",
    ]


def test_event_examples_validate_against_schemas() -> None:
    report = validate_contract_examples(Path("contracts"))

    assert report.issues == []
    assert len(report.examples_checked) == 3
