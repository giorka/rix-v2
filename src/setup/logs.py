import logging

from .config import Settings

import coloredlogs


def setup_logging(settings: Settings):
    level = logging.DEBUG if settings.is_debug else logging.INFO
    coloredlogs.install(level=level)
