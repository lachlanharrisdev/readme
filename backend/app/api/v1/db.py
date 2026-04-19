# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/db/utils.py
# Database utility functions for the V1 specification

from typing import Annotated

from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, Session, create_engine, select

from .settings import settings


def _get_connect_args(database_url: str) -> dict:
    # from fastapi sql tutorial; required for SQLite across threads.
    if database_url.startswith("sqlite"):
        return {"check_same_thread": False}
    return {}


engine: Engine = create_engine(
    settings.database_url,
    connect_args=_get_connect_args(settings.database_url),
    pool_pre_ping=True,
)


def create_db_and_tables() -> None:
    # import models to ensure registration with SQLModel
    # the 'noqa' tag fixes the linter whining about the unused import
    from . import models  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_engine() -> Engine:
    return engine


def get_session():
    with Session(engine) as session:
        yield session


# SessionDep is a dependency for injecting a database session into API endpoints
SessionDep = Annotated[Session, Depends(get_session)]


def ping_db(engine: Engine) -> None:
    with Session(engine) as session:
        session.exec(select(1)).one()
