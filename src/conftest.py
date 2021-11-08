import pytest
from django.test import AsyncClient as DjangoAsyncClient


class AsyncClient(DjangoAsyncClient):
    """Internal async test_client."""

    def post(self, *args, **kwargs):
        """Setup content-type header for all POST requests."""

        JSON_CONTENT_TYPE = "application/json"
        return super().post(*args, content_type=JSON_CONTENT_TYPE, **kwargs)


@pytest.fixture
def client():
    return AsyncClient()
