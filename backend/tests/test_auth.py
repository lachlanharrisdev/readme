# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This code is licensed under Apache 2.0
#
# Test file scoped to app/api/v1/auth


def test_auth_token_ok(client) -> None:
    res = client.post(
        "/api/v1/auth/token", data={"username": "lachlanharris", "password": "secret"}
    )
    assert res.status_code == 200
    assert "access_token" in res.json()
    assert res.json()["token_type"] == "bearer"


def test_auth_token_bad_credentials(client) -> None:
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


def test_auth_me_ok(client) -> None:
    token_res = client.post(
        "/api/v1/auth/token", data={"username": "lachlanharris", "password": "secret"}
    )
    access_token = token_res.json()["access_token"]

    res = client.get(
        "/api/v1/auth/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert res.status_code == 200
    body = res.json()
    assert body["username"] == "lachlanharris"
    assert isinstance(body["id"], int)
    assert "created_at" in body


def test_auth_me_no_token(client) -> None:
    res = client.get("/api/v1/auth/me")
    assert res.status_code == 401
    assert res.json()["detail"] == "Not authenticated"
