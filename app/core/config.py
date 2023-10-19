from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Beewise_Test'
    database_url: str = 'postgresql://user:password@postgresserver/db'

    class Config:
        env_file = '.env'


settings = Settings()
