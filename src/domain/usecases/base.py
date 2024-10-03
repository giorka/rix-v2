from abc import ABC, abstractmethod


class IUseCase(ABC):
    @abstractmethod
    async def __call__(self, *args, **kwargs):
        raise NotImplementedError()
