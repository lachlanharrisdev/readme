# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/main.py
# Main application file that establishes fastapi

from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from .api.v1.api import api_router
from .api.v1.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title="ReadMe Backend", version="0.1.0", lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")
