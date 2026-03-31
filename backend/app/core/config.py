import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CineMind AI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "b4661001c4ceeb08554dd755c328cb00c40e53a"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./cinemind.db"
    # Mapping dataset back up to the desktop dataset directory natively
    DATASET_PATH: str = r"C:\Users\RithinGude\Desktop\dataset"

    class Config:
        case_sensitive = True

settings = Settings()
