# pylint: disable=no-self-argument,no-self-use
from typing import Any, Dict, List, Literal, Optional

from pydantic import AnyHttpUrl, AnyUrl, PostgresDsn, SecretStr, validator, model_validator
from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    ENV: Literal["TEST", "DEV", "PROD"] = "DEV"

    SQL_DB: str
    SQL_HOST: str
    SQL_PORT: str
    SQL_USERNAME: str
    SQL_PASSWORD: str
    SQL_SSL: Optional[bool] = False

settings = Settings()
