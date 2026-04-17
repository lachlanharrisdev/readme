from __future__ import annotations

from sqlmodel import Session, create_engine, select
from sqlalchemy.engine import Engine

from .settings import settings


def get_engine() -> Engine:
    return create_engine(
        settings.database_url,
        pool_pre_ping=True,
    )


def ping_db(engine: Engine) -> None:
    with Session(engine) as session:
        session.exec(select(1)).one()
