from domain.auth.errors import AuthenticationError
from fastapi import Request, Response

from .custom_types import *

cookie_name = 'Authorization'


def get_token_from_request(r: Request) -> JsonWebToken:
    """
    Raises:
        AuthenticationError: User is not authenticated
    """

    token: JsonWebToken | None = r.cookies.get(cookie_name)

    if token is None:
        raise AuthenticationError

    return token


def set_token_to_response(r: Response, *, token: JsonWebToken, expires: ExpiresAt):
    r.set_cookie(cookie_name, token, expires=expires, httponly=True, secure=True)


def delete_cookie_from_response(r: Response):
    r.delete_cookie(cookie_name)
