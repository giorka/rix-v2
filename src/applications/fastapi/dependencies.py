from typing import Annotated

from fastapi import Depends

from domain.security import read_token, Payload, Credentials


def get_current_payload(token: Credentials) -> Payload:
    return read_token(token)


Payload = Annotated[Payload, Depends(get_current_payload)]
