import asyncio

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from applications.fastapi import get_application, get_server
from dependencies import (
    DatabaseProvider,
    RepositoryProvider,
    ServiceProvider,
    UseCaseProvider
)


async def main() -> None:
    application = get_application()

    setup_dishka(
        make_async_container(
            DatabaseProvider(),
            RepositoryProvider(),
            ServiceProvider(),
            UseCaseProvider()
        ),
        app=application
    )

    await get_server(application).serve()


if __name__ == '__main__':
    asyncio.run(main())
