from api.dt_api import DtApi
from api.ct_api import CTApi
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

    def test_get_container_number_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_tracking_by_any_number(number="TEMU1669697", type="CT", force_update=False, route=False, ais=False)
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_bl_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_tracking_by_any_number(number="ONEYOS3NA1938600", type="BL", force_update=False, route=False, ais=False)
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_bk_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_tracking_by_any_number(number="1811X023PE02032T1", type="BK", force_update=False, route=False, ais=False)
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"