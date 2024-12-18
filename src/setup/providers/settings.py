from setup.config import Settings

from dishka import Provider, Scope, provide


class SettingsProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_settings(self) -> Settings:
        return Settings()  # type: ignore
