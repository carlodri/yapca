import pytest
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from yapca.clockify import Clockify


class Settings(BaseSettings):
    model_config = SettingsConfigDict(secrets_dir="./tests/secrets")
    x_api_key: str


@pytest.fixture(scope="module")
def clockify_session():
    session = Clockify(Settings().x_api_key)
    yield session
    session.destroy()
