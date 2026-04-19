# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This code is licensed under Apache 2.0
#
# Test file for all basic health endpoints. These tests are meant to quickly fail
# and confirm the API is at least able to establish itself and basic listeners

from fastapi.testclient import TestClient
from sqlmodel import create_engine


def test_health_ok() -> None:
    from app.main import app

    client = TestClient(app)
    res = client.get("/api/v1/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
