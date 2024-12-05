import httpx

from yapca.clockify import Clockify
from yapca.models.user import User


def get_logged_in_user(clockify_session: Clockify) -> User:
    response = clockify_session.client.get(url="/user")
    print(response.json())
    assert response.status_code == httpx.codes.OK
    return User.model_validate(response.json())
