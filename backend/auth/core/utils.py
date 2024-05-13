from passlib.context import CryptContext

# Create a CryptContext object, this will be used for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using the specified CryptContext.
    :param password: The plain text password.
    :return: A hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against the hashed version.
    :param plain_password: The plain text password to verify.
    :param hashed_password: The hashed password to verify against.
    :return: True if the password is correct, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)
