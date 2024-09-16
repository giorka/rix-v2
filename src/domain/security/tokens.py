from dataclasses import dataclass, asdict
from datetime import timedelta
from typing import Annotated

from fastapi import Security
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials

from config import settings
from domain.entities import UserEntity
from .base import Token

jwt = JwtAccessBearer(secret_key=settings.singing_secret, refresh_expires_delta=timedelta(days=7))


@dataclass
class Payload:
    username: str


def get_user_payload(user: UserEntity) -> Payload:
    return Payload(username=user.username)


def make_token(user: UserEntity) -> Token:
    payload = asdict(get_user_payload(user))

    return jwt.create_refresh_token(payload)


def read_token(credentials: JwtAuthorizationCredentials) -> Payload:
    return Payload(username=credentials['username'])


Credentials = Annotated[JwtAuthorizationCredentials, Security(jwt)]
