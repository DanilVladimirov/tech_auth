import pydantic


class Settings(pydantic.BaseSettings):
    SECRET_KEY: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str = "localhost"
    DB_PORT: str = "5435"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 100
    JWT_ALGORITHM = "HS256"

    class Config:
        env_file = "../.env"
        case_sensitive = True


settings = Settings()
