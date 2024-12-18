from datetime import datetime

type CookieName = str
type CookieValue = str

type JsonWebToken = str
type ExpiresAt = datetime
type JsonWebTokenData = tuple[JsonWebToken, ExpiresAt]

__all__ = [
    'CookieName',
    'CookieValue',
    'JsonWebToken',
    'ExpiresAt',
    'JsonWebTokenData',
]
