from domain.base.error import BaseDomainError


class BaseAuthError(BaseDomainError):
    """Base error for auth errors"""


class AuthenticationError(BaseAuthError):
    """Raised when user is not authenticated"""

    message = 'User is not authenticated'


class AuthorizationError(BaseAuthError):
    """Raised when user failed to be authorized"""

    message = 'User failed to be authorized'
