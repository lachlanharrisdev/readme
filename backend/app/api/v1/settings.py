from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://app:app@127.0.0.1:5432/app"

    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )

settings = Settings()