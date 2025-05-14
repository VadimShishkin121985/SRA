import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_client():
    def _get_client(api_class, base_url=None):
        api_key = os.getenv("MY_API_KEY")  # <--- здесь
        return api_class(api_key=api_key, base_url=base_url) if base_url else api_class(api_key=api_key)
    return _get_client