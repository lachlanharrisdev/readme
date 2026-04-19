# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This code is licensed under Apache 2.0
#
# conftest.py
# Pytest configuration

import sys
from pathlib import Path

import os

import pytest
from fastapi.testclient import TestClient


BACKEND_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BACKEND_DIR))


# Ensure unit tests don't require a running Postgres instance.
# The application still defaults to Postgres for normal runs via settings.
TEST_DB_PATH = Path(__file__).resolve().parent / ".pytest.db"
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH}"


TEST_USER = {
    "username": "lachlanharris",
    "password": "secret",
}


@pytest.fixture
def client():
    from app.api.v1.db import create_db_and_tables, engine
    from app.main import app

    create_db_and_tables()

    with TestClient(app) as test_client:
        # seed the test user
        res = test_client.post("/api/v1/auth/signup", json=TEST_USER)
        if res.status_code not in (200, 409):
            raise RuntimeError(
                f"Failed to seed test user: {res.status_code} {res.text}"
            )
        yield test_client


@pytest.fixture(scope="session", autouse=True)
def run_after_all_tests():
    # pre-test code; pass
    yield
    # post-test code
    # delete the database file
    if TEST_DB_PATH.exists():
        TEST_DB_PATH.unlink()
