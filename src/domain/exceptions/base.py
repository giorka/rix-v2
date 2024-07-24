from dataclasses import dataclass


@dataclass(frozen=True)
class IException(Exception):
    """Base exception for the application"""

    pass
