from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # The base URL of the API
    HOST: str = "mongo"
    PORT: int = 27017
    DB_NAME: str = "mydatabase"
    COLLECTION_NAME: str = "mycollection"
    USERNAME: str = "root"
    PASSWORD: str = "example"

    class Config:
        env_file = ".env"


settings = Settings()
