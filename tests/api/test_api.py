from api.at_api import ATApi
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
        response = tracking_api.get_tracking_by_any_number(number="LYGU3109868", type="CT", force_update=False, route=False, ais=False)
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

    def test_route_information_by_cn(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_route_information_by_any_number(number="MSNU9731198", type="CT", sealine="MSCU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_route_information_by_bl(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_route_information_by_any_number(number="TAOE88677600", type="BL", sealine="HDMU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_route_information_by_bk(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_route_information_by_any_number(number="TAOF91227201", type="BK", sealine="HDMU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_shipping_line_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_shipping_line_info()
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_historical_data_cn(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_historical_data(number="DFSU6314506", type="CT", sealine="MSCU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_historical_data_bl(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_historical_data(number="ONEYOS3NA1705500", type="BL", sealine="ONEY")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_historical_data_bk(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_historical_data(number="EBKG06983286", type="BK", sealine="MSCU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_historical_data_id_ct(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_historical_data_id(id=436182293, number="DFSU6314506", type="CT", sealine="MSCU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_historical_data_id_bl(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_historical_data_id(id=436182293, number="ONEYOS3NA1705500", type="BL", sealine="ONEY")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_historical_data_id_bk(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_historical_data_id(id=436182293, number="EBKG06983286", type="BK", sealine="MSCU")
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_at_awb(self, api_client):
        air_tracking_api = api_client(ATApi)
        response = air_tracking_api.get_air_tracking_awb(number="157-89685002", path=True )
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"
