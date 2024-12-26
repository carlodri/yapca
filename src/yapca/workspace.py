from httpx import Client

from yapca.models.responses.get_all_workspaces import Workspace, Workspaces


class WorkspaceAPI:
    def __init__(self, client: Client):
        self._client = client

    def get_all_workspaces(self) -> Workspaces:
        response = self._client.get(url="/workspaces")
        response.raise_for_status()
        return Workspaces.model_validate(response.json())

    def get_workspace_info(self, workspace_id: str) -> Workspace:
        response = self._client.get(f"/workspaces/{workspace_id}")
        response.raise_for_status()
        return Workspace.model_validate(response.json())
