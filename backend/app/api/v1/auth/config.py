# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# src/api/v1/auth/env.py
# Manages authentication-specific env variables & constants

import os

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

fake_users_db = {
    "lachlanharris": {
        "username": "lachlanharris",
        "full_name": "Lachlan Harris",
        "email": "contact@lachlanharris.dev",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",  # "secret"
        "disabled": False,
    }
}

# Types
# -----


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
