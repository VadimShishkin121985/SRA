import pytest

@pytest.fixture
def api_client():
    """Универсальная фабрика API-клиентов."""
    def _get_client(api_class, base_url=None):
        return api_class(base_url=base_url) if base_url else api_class()
    return _get_client