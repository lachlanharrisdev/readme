# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This project is licensed under Apache 2.0
#
# app/api/v1/texts/endpoints.py
# Handles individual text endpoints

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.auth.auth import get_current_active_user
from app.api.v1.auth.config import User
from app.api.v1.db import SessionDep
from app.api.v1.models import TextDB

from sqlmodel import select


router = APIRouter()


@router.get("/texts/{text_id}", response_model=TextDB)
async def get_text(
    text_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: SessionDep,
):
    """
    Get a specific text by ID for the authenticated user

    Path Parameters:
        text_id: ID of the text to retrieve

    Response:
        TextDB

    Errors:
        404: text not found or does not belong to user
        500: unexpected error
    """

    text = session.exec(
        select(TextDB).where(TextDB.id == text_id, TextDB.user_id == current_user.id)
    ).first()

    if not text:
        raise HTTPException(status_code=404, detail="Text not found")

    return text
