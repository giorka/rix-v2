from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExceptionSchema:
    description: str
