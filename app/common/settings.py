from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # читаем .env (локальный, НЕ коммитим)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    APP_ENV: str = "dev"
    DB_URL: str = "postgresql+psycopg2://localdev:localpass@localhost:5432/crypto"
    REDIS_URL: str = "redis://localhost:6379/0"
    BINANCE_PROFILE: str = "testnet_umfutures"

@lru_cache
def get_settings() -> Settings:
    return Settings()
