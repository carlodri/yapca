from yapca.clockify_base import ClockifyBaseClient
from yapca.user import UserAPI
from yapca.workspace import WorkspaceAPI


class Clockify:
    def __init__(self, api_key: str):
        self._base = ClockifyBaseClient(api_key=api_key)
        self.user = UserAPI(self._base._client)
        self.workspace = WorkspaceAPI(self._base._client)

    def destroy(self):
        self._base._client.close()
