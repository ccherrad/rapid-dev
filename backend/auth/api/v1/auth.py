from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from auth.schemas.user import UserRegister


router = APIRouter(tags=["Authentication"], prefix="/auth")


@router.post("/register")
def register(
    user: UserRegister,
    session: AsyncSession = Depends(get_session),
):
    """
    """
    return {"status": user}
