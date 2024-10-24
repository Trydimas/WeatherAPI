from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_url: str
    apikey: str
    db_name: str
    db_pass: str
    db_host: str
    db_user: str
    db_port: str

    class Config:
        env_file = '.env'


settings = Settings()
