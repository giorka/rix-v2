from setup.app_factory import get_app, get_container
from setup.config import Settings
from setup.logs import setup_logging

import uvicorn


def main():
    settings = Settings()  # type: ignore

    setup_logging(settings)

    container = get_container(settings)
    app = get_app(container)

    uvicorn.run(app, host=settings.server.host, port=settings.server.port)


if __name__ == '__main__':
    main()
