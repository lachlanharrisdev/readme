# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/scheduling/config.py
# Manages scheduling-specific env variables & constants

from pydantic import BaseModel, Field, field_validator


class ScheduleForm(BaseModel):
    """
    Represents the post for a scheduling entry in the system
    with a dictionary of int 0-6 (weekdays) to int (minutes available)
    """

    availability: dict[int, int] = Field(
        ..., description="Map of weekday (0=Sun..6=Sat) to available minutes (0..1440)"
    )

    # because scheduling has a relatively complex data structure,
    # and browsers cannot be trusted, the data will be validated at
    # the API level
    @field_validator("availability")
    @classmethod
    def validate_availability(cls, value: dict[int, int]) -> dict[int, int]:
        if not isinstance(value, dict):
            raise ValueError("availability must be a dictionary")

        for day, minutes in value.items():
            if day not in range(7):
                raise ValueError("weekday must be an integer 0-6")
            if minutes < 0 or minutes > 1440:
                raise ValueError("minutes must be between 0 and 1440")

        return value
