# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/models.py
# SQLModel table models for the V1 specification.
#
# see https://dbdiagram.io/d/ReadMe-69e1d5ff0aa78f6bc1f6860e

from __future__ import annotations

from datetime import date, datetime
from enum import Enum

from sqlalchemy import Column, DateTime, UniqueConstraint, func
from sqlalchemy import Enum as SAEnum
from sqlmodel import Field, SQLModel


class TextType(str, Enum):
    book = "book"
    article = "article"
    paper = "paper"
    other = "other"


class UserDB(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
    )


class TextDB(SQLModel, table=True):
    __tablename__ = "texts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False, index=True)

    title: str = Field(nullable=False)
    author: str | None = None
    type: TextType | None = Field(
        default=None,
        sa_column=Column("type", SAEnum(TextType, name="text_type")),
    )

    total_pages: int | None = None
    is_mandatory: bool = Field(default=False, nullable=False)
    priority: int | None = None
    due_date: date | None = None

    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
    )


class AvailabilityDB(SQLModel, table=True):
    __tablename__ = "availability"
    __table_args__ = (UniqueConstraint("user_id", "day_of_week"),)

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
    day_of_week: int = Field(nullable=False)
    available_minutes: int | None = None
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )


class SessionDB(SQLModel, table=True):
    __tablename__ = "sessions"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
    text_id: int = Field(foreign_key="texts.id", nullable=False, index=True)

    scheduled_date: date = Field(nullable=False)
    pages_start: int | None = None
    pages_end: int | None = None
    duration_minutes: int | None = None
    is_completed: bool = Field(default=False, nullable=False)

    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
    )
