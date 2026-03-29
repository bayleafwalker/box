from pathlib import Path


def test_adr_declares_no_cross_service_database_access() -> None:
    adr = Path("docs/adr/0001-contract-first-platform.md").read_text(encoding="utf-8")
    assert "shared-database coupling" in adr
    assert "Every service owns its own persistence" in adr


def test_readme_mentions_phase_zero_assets() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "three initial service contracts" in readme
    assert "two scenario packs" in readme
