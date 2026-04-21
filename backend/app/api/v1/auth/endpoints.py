# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/auth.py
# JWT Authentication API endpoints according to the V1 specification

from .config import *
from .auth import *

import jwt

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from sqlmodel import select

from ..db import SessionDep
from ..models import UserDB

router = APIRouter()


# JWT-specific endpoints
# ----------------------


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep,
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
        401: if the username or password is incorrect
    """
    user = authenticate_user(session, form_data.username, form_data.password)
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


@router.post("/signup", response_model=User)
def signup(user: UserCreate, session: SessionDep) -> User:
    """Register a new user.

    Requires:
        username: string
        password: string

    Response:
        id: integer
        username: string
        created_at: timestamp

    Errors:
        409: if the username already exists
    """

    existing = session.exec(
        select(UserDB).where(UserDB.username == user.username)
    ).first()
    if existing:
        raise HTTPException(status_code=409, detail="Username already exists")

    db_user = UserDB(
        username=user.username, password_hash=get_password_hash(user.password)
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return User(id=db_user.id, username=db_user.username, created_at=db_user.created_at)


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
        id: integer
        username: string
        created_at: timestamp
    """
    return current_user
