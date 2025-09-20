from __future__ import annotations

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool
import os
import sys

# Логи Alembic
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Делаем импорт ваших пакетов доступным ---
# env.py находится в app/storage/migrations/env.py
# Поднимемся на 3 уровня до корня репозитория:
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if repo_root not in sys.path:
    sys.path.append(repo_root)

# Читаем .env (DB_URL и др.)
from dotenv import load_dotenv  # type: ignore
load_dotenv()

# Импортируем базу и модели
from app.common.settings import get_settings
from app.storage.db import Base
# ВАЖНО: импортируем файл models, чтобы Alembic «увидел» таблицы
from app.storage import models  # noqa: F401

# Метаданные для автогенерации миграций
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Запуск миграций в offline-режиме (без подключения)."""
    settings = get_settings()
    url = settings.DB_URL

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,  # сравнивать типы столбцов
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в online-режиме (с подключением к БД)."""
    settings = get_settings()

    configuration = config.get_section(config.config_ini_section) or {}
    configuration["sqlalchemy.url"] = settings.DB_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # сравнивать типы столбцов
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
