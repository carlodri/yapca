import pytest
from pydantic_settings import BaseSettings, SettingsConfigDict

from yapca.clockify import Clockify


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./tests/.env", secrets_dir="./tests/secrets"
    )
    x_api_key: str
    workspace_id: str
    user_id: str
    email: str


@pytest.fixture(scope="module")
def test_settings():
    print("run test_settings_func")
    return Settings()


@pytest.fixture(scope="module")
def clk_sess(test_settings):
    clk = Clockify(test_settings.x_api_key)
    yield clk
    clk.destroy()
