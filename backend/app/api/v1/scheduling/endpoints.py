# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/scheduling/endpoints.py
# Handles scheduling endpoints

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.auth.auth import get_current_active_user
from app.api.v1.auth.config import User
from app.api.v1.scheduling.config import ScheduleForm
from app.api.v1.db import SessionDep
from app.api.v1.models import AvailabilityDB

from sqlalchemy import delete
from sqlmodel import select

router = APIRouter()


@router.get("/schedule", response_model=ScheduleForm)
async def get_schedule(
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: SessionDep,  # type: ignore
) -> ScheduleForm:
    """
    return the authenticated user's current availability schedule

    Response:
        availability: Dictionary with keys as week days (int 0-6; 0 is Sunday)
            and values as integers for minutes available
            i.e. { 0: 30, 1: 40, 2: 0 ... }

    Errors:
        500: unexpected error
    """

    rows = session.exec(
        select(AvailabilityDB).where(AvailabilityDB.user_id == current_user.id)
    ).all()

    availability: dict[int, int] = {day: 0 for day in range(7)}
    for row in rows:
        # Defensive: ignore any malformed DB rows
        if row.day_of_week in availability and isinstance(row.available_minutes, int):
            availability[row.day_of_week] = row.available_minutes

    return ScheduleForm(availability=availability)


@router.post("/schedule", response_model=ScheduleForm)
async def submit_schedule(
    current_user: Annotated[User, Depends(get_current_active_user)],
    schedule: ScheduleForm,
    session: SessionDep,  # type: ignore
) -> ScheduleForm:
    """
    submit weekday availability schedule for the authenticated user,
    and adds it as separate entries to the `availability` table in
    the database

    Requires:
        schedule: Dictionary with keys as week days (int 0-6; 0 is Sunday)
            and values as integers for minutes available
            i.e. { 0: 30, 1: 40, 2: 0 ... }

    Errors:
        400: schedule format is invalid
        500: unexpected error

    """

    try:
        session.exec(
            delete(AvailabilityDB).where(AvailabilityDB.user_id == current_user.id)
        )

        # always store a full week; missing keys default to 0.
        entries = [
            AvailabilityDB(
                user_id=current_user.id,
                day_of_week=day,
                available_minutes=schedule.availability.get(day, 0),
            )
            for day in range(7)
        ]
        session.add_all(entries)
        session.commit()
    except Exception as exc:
        session.rollback()
        raise HTTPException(
            status_code=500, detail="Failed to update schedule"
        ) from exc

    return schedule
