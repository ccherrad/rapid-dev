from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(
    session: AsyncSession,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    dob: date = None
) -> User:
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        dob=dob
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
