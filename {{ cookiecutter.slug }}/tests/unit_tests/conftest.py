from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def unit_tests_dir() -> Path:
    """Absolute path for the /tests/unit_tests directory"""
    return Path(__file__).parent.resolve()
