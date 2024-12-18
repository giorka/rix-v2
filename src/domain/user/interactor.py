import logging

from domain.auth.errors import AuthenticationError, AuthorizationError
from domain.auth.ports.aup import AuthProvider
from domain.auth.ports.idp import IdentityProvider
from domain.base.interactor import BaseInteractor
from domain.ports.committer import Committer

from .custom_types import *
from .entity import UserEntity
from .errors import UserAlreadyExistsError
from .ports.repository import UserRepository
from .service import UserService

logger = logging.getLogger(__name__)


class UserInteractor(BaseInteractor):
    def __init__(
        self,
        *,
        user_service: UserService,
        user_repo: UserRepository,
        idp: IdentityProvider,
        auth: AuthProvider,
        committer: Committer,
    ):
        self._user_service = user_service
        self._user_repo = user_repo
        self._auth = auth
        self._idp = idp
        self._committer = committer

    async def register(self, username: Username, password: Password) -> UserEntity:
        """
        Register User

        Raises:
            UserAlreadyExistsError: Raised when trying to create a user that already exists
        """

        if await self._user_repo.get_by_username(username) is not None:
            logger.info('User already exists')
            raise UserAlreadyExistsError(username)

        user_entity = self._user_service.create_user(username, password)

        logger.info(f'User {user_entity} created')

        await self._user_repo.create(user_entity)
        await self._committer.commit()

        await self._auth.login(username)

        return user_entity

    async def login(self, username: Username, password: Password) -> UserEntity:
        """
        Login User

        Raises:
            AuthorizationError: Raised when user failed to be authorized
        """

        user = await self._user_repo.get_by_username(username)
        logger.debug(f'{user=}')

        if user is None or not self._user_service.check_password(user, password):
            logging.info(f'User could not log in')
            raise AuthorizationError

        logging.info(f'User successfully logged in')

        await self._auth.login(username)

        return user

    async def get_current_user(self) -> UserEntity:
        """
        Get Current User

        Raises:
            AuthenticationError: Raised when user is not authenticated
        """

        current_username = await self._idp.get_username()
        logger.debug(f'{current_username=}')
        current_user = await self._user_repo.get_by_username(current_username)
        logger.debug(f'{current_user=}')

        if current_user is None:
            logging.info('User is unauthorized')
            raise AuthenticationError

        return current_user

    async def logout(self):
        """
        Logout Current User

        Raises:
            None
        """

        await self._auth.logout()
