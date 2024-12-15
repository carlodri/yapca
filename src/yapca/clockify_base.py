import httpx

from yapca.config import settings


class ClockifyBaseClient:
    def __init__(self, api_key: str):
        headers = {"x-api-key": api_key}
        self._client = httpx.Client(
            base_url=str(settings.clockify_api_url), headers=headers
        )
