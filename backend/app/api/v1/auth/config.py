# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/auth/env.py
# Manages authentication-specific env variables & constants

import os
from datetime import datetime

from dotenv import load_dotenv

from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from pydantic import BaseModel

# Environment variable loading
# ----------------------------
load_dotenv()

SECRET_KEY = os.getenv(
    "SECRET_KEY", "8f70b2b1dd185be4d29bbfeeba2f98b588b6653c857d5d29bc77fd7e14b8dcc9"
)
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "300"))

# Constants
# ---------

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

# Types
# -----


class Token(BaseModel):
    """
    Represents a JWT access token response
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Represents the data contained within a JWT access token
    """

    username: str | None = None


class User(BaseModel):
    """
    Represents a user in the system, excluding sensitive information
    for the purpose of API responses (i.e. /api/v1/auth/me)
    """

    id: int
    username: str
    created_at: datetime | None = None


class UserInDB(User):
    """
    Represents a user in the database, including sensitive information
    """

    password_hash: str


class UserCreate(BaseModel):
    """
    Represents the data required to create a new user account
    """

    username: str
    password: str
