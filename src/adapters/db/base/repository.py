import abc

from sqlalchemy.ext.asyncio import AsyncSession


class BaseAlchemyRepository(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
