from api.dt_api import DtApi
import pytest

@pytest.mark.usefixtures("api_client")
class TestApi():
    def test_get_road_distance(self, api_client):
        distance_api = api_client(DtApi)
        response = distance_api.get_distance(from_city="madrid", to_city="ibiza", transport_mode='road')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

    def test_get_sea_distance(self, api_client):
        distance_api = api_client(DtApi)
        response = distance_api.get_distance(from_city="istanbul", to_city="kiev", transport_mode='sea, road')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

    def test_get_air_distance(self, api_client):
        distance_api = api_client(DtApi)
        response = distance_api.get_distance(from_city="istandul", to_city="kiev", transport_mode='air')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

    def test_get_rail_distance(self, api_client):
        distance_api = api_client(DtApi)
        response = distance_api.get_distance(from_city='tampa', to_city='toronto', transport_mode='rail, road')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

    def test_get_rail_locode_distance(self, api_client):
        distance_api = api_client(DtApi)
        response = distance_api.get_distance(from_city='UAODS', to_city='UALVV', transport_mode='rail, road')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

    def test_get_air_decimal_coordinate_distance(self, api_client):
        distance_api = api_client(DtApi)
        response = distance_api.get_distance(from_city="34.543896, 69.160652", to_city="13.696784, 100.5056763", transport_mode='air, road')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

