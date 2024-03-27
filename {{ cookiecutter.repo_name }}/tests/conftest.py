import shutil
import uuid
from pathlib import Path
from typing import Generator

import platformdirs
import pytest
from loguru import logger


@pytest.fixture(scope="session")
def tests_dir() -> Path:
    """Absolute path for the /tests directory"""
    return Path(__file__).parent.resolve()


@pytest.fixture()
def temp_dir() -> Generator[Path, None, None]:
    """Create a new unique temp dir that gets cleaned up after tests"""
    tmp: Path = platformdirs.user_data_path(appname="{{ cookiecutter.repo_name }}") / "temp" / str(uuid.uuid4())
    # Make this dir and any parents it needs, but error if it already exists
    logger.debug(f"Creating temp dir: {tmp}")
    tmp.mkdir(parents=True, exist_ok=False)
    yield tmp
    # Clean up
    logger.debug(f"Removing temp dir: {tmp}")
    shutil.rmtree(tmp)
