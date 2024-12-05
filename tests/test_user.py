from yapca.clockify import Clockify
from yapca.user import get_logged_in_user


def test_get_logged_in_user(clockify_session):
    user = get_logged_in_user(clockify_session)
