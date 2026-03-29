from pathlib import Path

from packages.scenario_sdk.validation import validate_scenarios


def test_scenario_packs_validate() -> None:
    report = validate_scenarios(
        Path("scenario-packs"),
        Path("schemas/scenario-pack.schema.json"),
        known_services={"party-service", "catalog-service", "transaction-service"},
    )

    assert report.issues == []
    assert report.scenarios == ["hotdog-stand", "it-consultancy"]
