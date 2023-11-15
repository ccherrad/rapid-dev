from datetime import datetime, timedelta
from typing import Optional, Tuple, Union
from urllib.parse import urljoin

from fastapi import Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.users import get_user
from ..models.users import User
from ..schemas.token import TokenPayload
from ..schemas.user import UserStatus
from .config import settings
from .database import get_session


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Gets the password text and gets its hash.

    Args:
        password (str): Password.

    Returns:
        str: Password hash.
    """
    return password_context.hash(password)


def is_valid_password(plain_password: str, hashed_password: str) -> bool:
    """Check if given password matches user's hashed password.

    Args:
        plain_password (str): Possible user's password.
        hashed_password (str): User's hashed password.

    Returns:
        bool: True, if matches, False otherwise.
    """
    return password_context.verify(plain_password, hashed_password)


async def authenticate(
    session: AsyncSession, email: EmailStr, password: str
) -> Optional[User]:
    """Authenticate user from their email and password.

    Args:
        session (AsyncSession): Database session.
        email (EmailStr): User's email.
        password (str): User's password.

    Returns:
        Optional[User]: User object if validated.
    user = await get_user(session, with_groups=True, email=email)

    if not user:
        return None

    if user.status is not UserStatus.INACTIVE:
        policy = await get_password_policy_by_org_id(session, user.org_id)

        if not is_valid_password(password, user.hashed_password):
            user.login_attempts += 1
            if user.login_attempts >= policy.max_login_attempts:
                user.status = UserStatus.BLOCKED

            await session.commit()

            return None

        if (
            user.password_updated_on is None
            or (user.password_updated_on + timedelta(days=policy.expiration))
            < datetime.utcnow()
        ):
            user.status = UserStatus.EXPIRED

            await session.commit()

            return user

    user.login_attempts = 0
    user.last_login_on = datetime.utcnow()

    await session.commit()

    return user
    """
    pass

