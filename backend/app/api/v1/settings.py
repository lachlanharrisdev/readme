# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/settings.py
# Application settings for the V1 specification

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # compose sets DATABASE_URL to the correct postgres url. pytest sets it to a local sqlite file db
    # (backend/.pytest.db). if not set (i.e. local dev), if not set, fall back to a local automatically
    # created sqlite file DB
    database_url: str = "sqlite:///./database.db"

    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )


settings = Settings()
