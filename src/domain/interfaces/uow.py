from typing import Protocol


class AsyncUnitOfWork(Protocol):
    async def commit(self, *args, **kwargs) -> None: pass

    async def rollback(self, *args, **kwargs) -> None: pass
