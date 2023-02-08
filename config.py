from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./master_database.db"

    class Config:
        env_file = ".env"


settings = Settings()
