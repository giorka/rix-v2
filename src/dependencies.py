from typing import AsyncIterable

from dishka import provide, Provider, Scope
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, AsyncSession, create_async_engine

from config import settings


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_engine(self) -> AsyncEngine:
        return create_async_engine(
            settings.db_url,
            echo=False,
            pool_recycle=180
        )

    @provide(scope=Scope.APP)
    def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(self, factory: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        session = factory()

        yield session

        await session.close()
