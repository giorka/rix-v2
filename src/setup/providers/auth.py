from adapters.auth.fastapi.aup import FastapiAuthProviderImpl
from adapters.auth.fastapi.idp import FastapiIdentityProviderImpl
from adapters.auth.fastapi.token_processor import TokenProcessorImpl
from domain.auth.ports.aup import AuthProvider
from domain.auth.ports.idp import IdentityProvider
from setup.config import Settings

from dishka import Provider, Scope, from_context, provide
from fastapi import Request
from jwt import PyJWT
from redis.asyncio import Redis


class AuthDependencyProvider(Provider):
    scope = Scope.REQUEST

    request = from_context(Request, scope=Scope.REQUEST)

    @provide(scope=Scope.APP)
    def get_jwt(self) -> PyJWT:
        return PyJWT()

    @provide(scope=Scope.APP)
    def get_redis(self, settings: Settings) -> Redis:
        return Redis.from_url(str(settings.redis))

    @provide
    def get_token_processor(self, jwt: PyJWT, r: Redis, settings: Settings) -> TokenProcessorImpl:
        return TokenProcessorImpl(jwt=jwt, r=r, settings=settings)

    @provide
    def get_identity_provider(self, req: Request, token_processor: TokenProcessorImpl) -> IdentityProvider:
        return FastapiIdentityProviderImpl(req, token_processor=token_processor)

    @provide
    def get_auth_provider(self, req: Request, token_processor: TokenProcessorImpl) -> AuthProvider:
        return FastapiAuthProviderImpl(req, token_processor=token_processor)
