from sqlalchemy.orm import Session
from auth.models.user import User
from auth.core.utils import hash_password, verify_password

def create_user(db: Session, user_data: dict) -> User:
    """
    Create a normal user with hashed password and set is_superuser to False.

    :param db: SQLAlchemy Session instance.
    :param user_data: Dictionary containing user data.
    :return: User instance created.
    """
    user_data["password"] = hash_password(user_data["password"])
    user_data["is_superuser"] = False
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_superuser(db: Session, user_data: dict) -> User:
    """
    Create a superuser with hashed password and set is_superuser to True.

    :param db: SQLAlchemy Session instance.
    :param user_data: Dictionary containing user data.
    :return: User instance created.
    """
    user_data["password"] = hash_password(user_data["password"])
    user_data["is_superuser"] = True
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> User:
    """
    Retrieve a user by their ID.

    :param db: SQLAlchemy Session instance.
    :param user_id: The ID of the user to retrieve.
    :return: User instance if found, None otherwise.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    """
    Retrieve a user by their email.

    :param db: SQLAlchemy Session instance.
    :param email: Email address of the user to retrieve.
    :return: User instance if found, None otherwise.
    """
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: int, update_data: dict) -> User:
    """
    Update user details.

    :param db: SQLAlchemy Session instance.
    :param user_id: The ID of the user to update.
    :param update_data: Dictionary containing data to update.
    :return: Updated User instance.
    """
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> bool:
    """
    Delete a user by their ID and return True if successful.

    :param db: SQLAlchemy Session instance.
    :param user_id: The ID of the user to delete.
    :return: True if deletion was successful, False otherwise.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


def authenticate(db: Session, email: str, password: str) -> bool:
    """
    Authenticate a user by verifying their email and password.

    :param db: SQLAlchemy Session instance.
    :param email: Email address of the user to authenticate.
    :param password: Password provided for authentication.
    :return: True if authentication is successful, False otherwise.
    """
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.password):
        return True
    return False

