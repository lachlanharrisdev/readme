# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This code is licensed under Apache 2.0
#
# Test file for database functionality. confirms the connection between the API and the DB,
# and runs through the non-api-endpoint db logic. limted for now

from fastapi.testclient import TestClient
from sqlmodel import create_engine


def test_db_connection() -> None:
    from app.main import app

    client = TestClient(app)
    res = client.get("/api/v1/health/db")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
