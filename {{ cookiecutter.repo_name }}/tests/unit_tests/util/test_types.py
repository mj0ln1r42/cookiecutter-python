from pathlib import Path

from {{ cookiecutter.package_name }}.util.types import *


def _create_file(filename: PathLike) -> bool:
    """Convert a PathLike to a Path, create the file and return its existence."""
    file: Path = ToPath(filename)
    file.touch()
    return file.exists()


def test_PathLike_str(temp_dir: Path) -> None:
    str_path: str = str(temp_dir / "str")
    assert _create_file(str_path)


def test_PathLike_bytes(temp_dir: Path) -> None:
    bytes_path: bytes = bytes(temp_dir / "bytes")
    assert _create_file(bytes_path)


def test_PathLike_Path(temp_dir: Path) -> None:
    path_path: Path = temp_dir / "path"
    assert _create_file(path_path)
