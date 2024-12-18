from logging.config import fileConfig

from alembic import context
from infrastructure.alchemy.models import IModel
from sqlalchemy import engine_from_config, pool

config = context.config


options = {
    "sqlalchemy.url": str(config.get_main_option("sqlalchemy.url"))
    + "?async_fallback=True"
}

for name, value in options.items():
    config.set_main_option(name, value)


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = IModel.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
