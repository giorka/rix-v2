from typing import Annotated

from domain.security import Credentials, Payload, read_token
from fastapi import Depends


def get_current_payload(token: Credentials) -> Payload:
    return read_token(token)


Payload = Annotated[Payload, Depends(get_current_payload)]
