from typing import List

from httpx import Client

from yapca.models.get_member_profile import Member
from yapca.models.get_user import User, Users


class UserAPI:
    def __init__(self, client: Client):
        self._client = client

    def get_logged_in_user(self) -> User:
        response = self._client.get(url="/user")
        response.raise_for_status()
        return User.model_validate(response.json())

    def find_all_users_in_workspace(self, workspace_id: str) -> List[User]:
        response = self._client.get(url=f"/workspaces/{workspace_id}/users")
        response.raise_for_status()
        users_model = Users.model_validate(response.json())
        return users_model.root

    def get_member_profile(self, workspace_id: str, user_id: str) -> Member:
        response = self._client.get(
            url=f"/workspaces/{workspace_id}/member-profile/{user_id}"
        )
        response.raise_for_status()
        return Member.model_validate(response.json())
