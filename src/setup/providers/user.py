from adapters.db.user.repository import UserAlchemyRepositoryImpl
from adapters.user.hasher import HasherImpl
from domain.auth.ports.aup import AuthProvider
from domain.auth.ports.idp import IdentityProvider
from domain.user.interactor import UserInteractor
from domain.user.ports.hasher import Hasher
from domain.user.ports.repository import UserRepository
from domain.user.service import UserService
from setup.config import Settings
from setup.providers.db import AsyncSession

from argon2 import PasswordHasher
from dishka import Provider, Scope, provide


class UserDependencyProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    def get_low_level_hasher(self) -> PasswordHasher:
        return PasswordHasher()

    @provide
    def get_hasher(self, h: PasswordHasher, settings: Settings) -> Hasher:
        return HasherImpl(hasher=h, settings=settings)

    @provide
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserAlchemyRepositoryImpl(session)

    @provide
    def get_user_service(self, h: Hasher) -> UserService:
        return UserService(h)

    @provide
    def get_user_interactor(
        self,
        user_service: UserService,
        user_repo: UserRepository,
        auth: AuthProvider,
        idp: IdentityProvider,
        committer: AsyncSession,
    ) -> UserInteractor:
        return UserInteractor(
            user_service=user_service,
            user_repo=user_repo,
            auth=auth,
            idp=idp,
            committer=committer,
        )
