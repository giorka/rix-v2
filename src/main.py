import asyncio

from authlib.jose.errors import BadSignatureError
from starlette import responses

from applications.fastapi import get_application, get_server


async def main() -> None:
    application = get_application()

    @application.exception_handler(BadSignatureError)
    async def handle_bad_signature_error(*args, **kwargs) -> responses.Response:
        return responses.JSONResponse(
            status_code=401,
            content={'detail': 'Credentials are not provided'},
        )

    await get_server(application).serve()


if __name__ == '__main__':
    asyncio.run(main())
