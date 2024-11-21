import httpx


class Clockify:
    def __init__(self, api_key):
        headers = {"x-api-key": api_key}
        self.http_client = httpx.Client(headers=headers)
