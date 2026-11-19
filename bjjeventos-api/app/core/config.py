import os
try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseModel
    class BaseSettings(BaseModel):
        pass

class Settings(BaseSettings):
    PROJECT_NAME: str = "BJJEventOS API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "bjj_secret_key_change_in_production_98765")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./bjjeventos.db")

settings = Settings()
