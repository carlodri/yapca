import httpx

from yapca.config import settings


class Clockify:
    def __init__(self, api_key):
        headers = {"x-api-key": api_key}
        self.client = httpx.Client(
            base_url=str(settings.clockify_api_url), headers=headers
        )

    def destroy(self):
        self.client.close()
