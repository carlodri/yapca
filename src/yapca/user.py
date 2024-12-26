from typing import List, Optional

from httpx import Client
from pydantic import validate_call

from yapca.models.query_parameters.find_all_users_in_workspace import (
    GetUsersQueryParams,
)
from yapca.models.responses.get_member_profile import Member
from yapca.models.responses.get_user import User, Users


class UserAPI:
    def __init__(self, client: Client):
        self._client = client

    @validate_call
    def get_logged_in_user(self, include_memberships: bool = False) -> User:
        response = self._client.get(
            url="/user", params={"include-memberships": include_memberships}
        )
        response.raise_for_status()
        return User.model_validate(response.json())

    @validate_call
    def find_all_users_on_workspace(
        self,
        workspace_id: str,
        query_parameters: GetUsersQueryParams = GetUsersQueryParams(),
    ) -> List[User]:
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
