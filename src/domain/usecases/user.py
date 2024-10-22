from domain import exceptions, security
from ..interfaces.uow import AsyncUnitOfWork
from ..services import UserService
from .base import IUseCase


class RegisterUserUseCase(IUseCase):
    """
    Register user
    """

    def __init__(self, user_service: UserService, uow: AsyncUnitOfWork) -> None:
        self.user_service = user_service
        self._uow = uow

    async def __call__(self, username: str, password: str) -> JWT:
        """
        Register user

        Args:
            username (Username): User username
            password (Password): User password

        Raises:
            exceptions.UserAlreadyExistsException: Raises when there is already a user

        Returns:
            JWT: User JWT
        """

        hashed_password = security.make_password(password)
        user_entity = await self.user_service.register(username, hashed_password)

        await self._uow.commit()

        token = security.make_token(user_entity)

        return token
