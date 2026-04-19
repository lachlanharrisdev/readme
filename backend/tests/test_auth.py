# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This code is licensed under Apache 2.0
#
# Test file scoped to src/api/v1/auth

from fastapi.testclient import TestClient


def test_auth_token_ok() -> None:
    from app.main import app

    client = TestClient(app)
    res = client.post(
        "/api/v1/auth/token", data={"username": "lachlanharris", "password": "secret"}
    )
    assert res.status_code == 200
    assert "access_token" in res.json()
    assert res.json()["token_type"] == "bearer"


def test_auth_token_bad_credentials() -> None:
    from app.main import app

    client = TestClient(app)
    res = client.post(
        "/api/v1/auth/token",
        data={"username": "lachlanharris", "password": "wrongpassword"},
    )
    assert res.status_code == 401
    assert res.json()["detail"] == "Incorrect username or password"

    res = client.post(
        "/api/v1/auth/token", data={"username": "mr-i-dont-exist", "password": "secret"}
    )
    assert res.status_code == 401
    assert res.json()["detail"] == "Incorrect username or password"


def test_auth_me_ok() -> None:
    from app.main import app

    client = TestClient(app)
    token_res = client.post(
        "/api/v1/auth/token", data={"username": "lachlanharris", "password": "secret"}
    )
    access_token = token_res.json()["access_token"]

    res = client.get(
        "/api/v1/auth/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert res.status_code == 200
    assert res.json() == {
        "username": "lachlanharris",
        "full_name": "Lachlan Harris",
        "email": "contact@lachlanharris.dev",
        "disabled": False,
    }


def test_auth_me_no_token() -> None:
    from app.main import app

    client = TestClient(app)
    res = client.get("/api/v1/auth/me")
    assert res.status_code == 401
    assert res.json()["detail"] == "Not authenticated"
