from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    debug: bool = True
    secret_key: str
    tg_bot_token: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
