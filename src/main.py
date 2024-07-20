import asyncio

from applications.fastapi import get_application, get_server


async def main() -> None:
    application = get_application()

    await get_server(application).serve()


if __name__ == '__main__':
    asyncio.run(main())
