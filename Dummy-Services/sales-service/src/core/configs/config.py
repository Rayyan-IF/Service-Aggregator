import os
from pydantic import Field
from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env_paths: ClassVar[list[str]] = ['.env', '../../../.env']
    env_path: ClassVar[str] = next((path for path in env_paths if os.path.exists(path)), None)
    model_config = SettingsConfigDict(env_file=env_path, env_file_encoding="utf-8")

    db_user: str = Field(...,alias="DB_USER")
    db_name: str = Field(...,alias="DB_NAME")
    db_port: str = Field(...,alias="DB_PORT")
    db_driver: str = Field(...,alias="DB_DRIVER")
    db_server: str = Field(...,alias="DB_SERVER")
    db_password: str = Field(...,alias="DB_PASSWORD")
