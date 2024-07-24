from dataclasses import dataclass

from . import IException


@dataclass(frozen=True)
class IValidationException(IException):
    pass
