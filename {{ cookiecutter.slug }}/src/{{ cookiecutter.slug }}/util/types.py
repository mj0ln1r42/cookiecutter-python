"""Custom Typing Definitions

This file defines custom type aliases and generics used across the project.
These types enhance code readability and type checking.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Generic
from typing import SupportsBytes
from typing import TypeVar
from typing import Union
from typing import cast

from typing_extensions import ParamSpec


P = ParamSpec("P")
P2 = ParamSpec("P2")
T = TypeVar("T")
U = TypeVar("U")

PathLike = TypeVar("PathLike", str, bytes, os.PathLike)


def ToPath(path: PathLike) -> Path:
    if isinstance(path, bytes):
        return Path(os.fsdecode(path))
    return Path(path)
