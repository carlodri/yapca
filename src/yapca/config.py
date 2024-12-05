from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    clockify_api_url: HttpUrl = "https://api.clockify.me/api/v1/"


settings = Settings()
