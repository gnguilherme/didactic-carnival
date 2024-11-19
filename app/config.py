from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # The base URL of the API
    HOST: str = "localhost"
    PORT: int = 27017
    DB_NAME: str = "mydatabase"
    COLLECTION_NAME: str = "mycollection"

    class Config:
        env_file = ".env"


settings = Settings()
