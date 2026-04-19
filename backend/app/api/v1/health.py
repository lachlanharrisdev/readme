# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# src/api/v1/health.py
# Health check API endpoints according to the V1 specification

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.engine import Engine

from .db import get_engine, ping_db

router = APIRouter()


@router.get("/")
def health_check():
    """
    Health check endpoint to verify that the API is running and responsive.

    Response:
        status: string ("ok")

    Errors:
        500 Internal Server Error: If the API is not healthy
    """
    return {"status": "ok"}


@router.get("/db")
def health_check_db(engine: Engine = Depends(get_engine)):
    """
    Health check endpoint to verify that the database connection is healthy.

    Response:
        status: string ("ok")

    Errors:
        500 Internal Server Error: If the database connection is not healthy
    """
    try:
        ping_db(engine)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection failed") from e
