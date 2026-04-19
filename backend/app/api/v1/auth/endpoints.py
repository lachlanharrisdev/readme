# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# src/api/v1/auth.py
# JWT Authentication API endpoints according to the V1 specification

from .config import *
from .auth import *

import jwt

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter()


# JWT-specific endpoints
# ----------------------


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """
    Request a JWT access token by providing a username and password

    Requires:
        username: string
        password: string

    Response:
        access_token: string
        token_type: string ("bearer")

    Errors:
        401 Unauthorized: If the username or password is incorrect
    """
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


# Utilities
# ---------


@router.get("/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    """
    Get the current authenticated user's information

    Authorization: true

    Response:
        username: string
        email: string
        full_name: string
        disabled: boolean
    """
    return current_user
