from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    visual_crossing_api_key: str  # Se lee automáticamente del .env

    class Config:
        env_file = ".env"

settings = Settings()
