from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix = "", case_sensitive = False, env_file = ".env", env_file_encoding = 'utf-8')

    db_name: str = Field(...,alias="DB_NAME")
    db_user: str = Field(...,alias="DB_USER")
    db_port: str = Field(...,alias="DB_PORT")
    db_driver: str = Field(...,alias="DB_DRIVER")
    db_server: str = Field(...,alias="DB_SERVER")
    db_password: str = Field(...,alias="DB_PASSWORD")