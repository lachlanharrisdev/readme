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


@router.get("/{text_id}", response_model=TextDB)
async def get_text(
    text_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: SessionDep,  # type: ignore
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


@router.post("/new", response_model=TextDB)
async def new_text(
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: SessionDep,  # type: ignore
    text: TextDB,
):
    """
    Create a new text for the authenticated user

    Requires:
        text: text content

    Errors:
        400: invalid request body
        500: unexpected error
    """

    """
    {
        "id": 0,
        "user_id": 0,
        "title": "string",
        "author": "string",
        "type": "book",
        "total_pages": 0,
        "is_mandatory": false,
        "priority": 0,
        "due_date": "2026-05-03",
        "created_at": "2026-05-03T23:24:00.335Z"
    }
    """
    text.user_id = current_user.id

    # database will determine these values
    text.id = None
    text.created_at = None

    session.add(text)
    session.commit()
    session.refresh(text)

    return text


@router.delete("/{text_id}", status_code=204)
async def delete_text(
    text_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: SessionDep,  # type: ignore
):
    """
    Delete a specific text by ID for the authenticated user

    Path Parameters:
        text_id: ID of the text to delete

    Response:
        204: text deleted successfully

    Errors:
        404: text not found or does not belong to user
        500: unexpected error
    """

    text = session.exec(
        select(TextDB).where(TextDB.id == text_id, TextDB.user_id == current_user.id)
    ).first()

    if not text:
        raise HTTPException(status_code=404, detail="Text not found")

    session.delete(text)
    session.commit()

    return


@router.put("/{text_id}", response_model=TextDB)
async def update_text(
    text_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: SessionDep,  # type: ignore
    updated_text: TextDB,
):
    """
    Update a specific text by ID for the authenticated user

    Path Parameters:
        text_id: ID of the text to update

    Requires:
        text: updated text content

    Response:
        TextDB

    Errors:
        404: text not found or does not belong to user
        400: invalid request body
        500: unexpected error
    """

    text = session.exec(
        select(TextDB).where(TextDB.id == text_id, TextDB.user_id == current_user.id)
    ).first()

    if not text:
        raise HTTPException(status_code=404, detail="Text not found")

    text.title = updated_text.title
    text.author = updated_text.author
    text.type = updated_text.type
    text.total_pages = updated_text.total_pages
    text.is_mandatory = updated_text.is_mandatory
    text.priority = updated_text.priority
    text.due_date = updated_text.due_date

    session.add(text)
    session.commit()
    session.refresh(text)

    return text
