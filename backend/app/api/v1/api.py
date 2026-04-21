# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/api.py
# Primary API router for V1. This file can be considered the
# "main" file for the API

from fastapi import APIRouter

from .auth import endpoints as auth_endpoints
from .scheduling import endpoints as scheduling_endpoints
from . import health

api_router = APIRouter()
api_router.include_router(auth_endpoints.router, prefix="/auth", tags=["auth"])

api_router.include_router(
    scheduling_endpoints.router, prefix="/scheduling", tags=["scheduling"]
)

api_router.include_router(health.router, prefix="/health", tags=["health"])
