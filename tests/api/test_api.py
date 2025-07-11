from datetime import datetime

from api.ai_api import AIApi
from api.at_api import ATApi
from api.dt_api import DtApi
from api.ct_api import CTApi
import pytest

from api.parcel_api import ParcelApi
from api.ss_api import SSApi



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
        response = distance_api.get_distance(from_city="istandul", to_city="kiev", transport_mode='air, road')
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
        response = distance_api.get_distance(from_city="34.543896, 69.160652", to_city="13.696784, 100.5056763",
                                             transport_mode='air, road')
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True, "API response 'success' is not True"

    def test_get_container_number_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_tracking_by_any_number(number="LYGU3109868", type="CT", force_update=False,
                                                           route=False, ais=False)
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_bl_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_tracking_by_any_number(number="ONEYOS3NA1938600", type="BL", force_update=False,
                                                           route=False, ais=False)
        data = response.json()
        assert response.status_code == 200
        assert data["status"] != "error", f"Unexpected error: {data.get('message')}"

    def test_get_bk_info(self, api_client):
        tracking_api = api_client(CTApi)
        response = tracking_api.get_tracking_by_any_number(number="1811X023PE02032T1", type="BK", force_update=False,
                                                           route=False, ais=False)
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
        response = tracking_api.get_historical_data_id(id=436182293, number="ONEYOS3NA1705500", type="BL",
                                                       sealine="ONEY")
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

    def test_ss_get_schedules_by_points_general_cargo(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_points_general_cargo(cargo_type="GC", origin="CNSHG",
                                                                            destination="DEHAM", from_date=from_date,
                                              weeks=4, sort="DEP", direct_only=False, multimodal=True)
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_points_general_cargo_sort_arrival(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_points_general_cargo(cargo_type="GC", origin="CNSHG",
                                                                            destination="DEHAM", from_date=from_date,
                                              weeks=4, sort="ARR", direct_only=False, multimodal=True)
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_points_general_cargo_sort_transit_time(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_points_general_cargo(cargo_type="GC", origin="CNSHG",
                                                                            destination="DEHAM", from_date=from_date,
                                              weeks=4, sort="TT", direct_only=False, multimodal=True)
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_points_reefer(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_points_general_cargo(cargo_type="REEF", origin="CNSHG",
                                                                            destination="DEHAM", from_date=from_date,
                                              weeks=4, sort="DEP", direct_only=False, multimodal=True)
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_points_ro_ro(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_points_general_cargo(cargo_type="RORO", origin="CNSHG",
                                                                            destination="DEHAM", from_date=from_date,
                                              weeks=4, sort="DEP", direct_only=False, multimodal=True)
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_points_lcl(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_points_general_cargo(cargo_type="LCL", origin="CNSHG",
                                                                            destination="DEHAM", from_date=from_date,
                                              weeks=4, sort="DEP", direct_only=False, multimodal=True)
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_vessel(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_vessel(imo=9780847, )
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_by_ports(self, api_client):
        from_date = datetime.now().strftime('%Y-%m-%d')
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_by_ports(locode="USNYC", from_date=from_date, weeks=4 )
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_points_general_cargo(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_POINTS", cargo_type="GC")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_points_reefer(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_POINTS", cargo_type="REEF")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_points_ro_ro(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_POINTS", cargo_type="RORO")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_points_lcl(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_POINTS", cargo_type="LCL")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_vessel_general_cargo(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_VESSEL", cargo_type="GC")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_vessel_reefer(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_VESSEL", cargo_type="REEF")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_vessel_ro_ro(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="VESSEL", cargo_type="RORO")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carriers_by_vessel_lcl(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carriers(schedule_type="BY_VESSEL", cargo_type="LCL")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carrier_entry_scac(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carrier_entry_scac(scac="ACLU")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_carrier_entry_imo(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_carrier_entry_imo(imo="9588081")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ss_get_schedules_ports_entry(self, api_client):
        ship_schedules_api = api_client(SSApi)
        response = ship_schedules_api.get_schedules_port_entry(locode="USNYC")
        data = response.json()
        assert response.status_code == 200
        assert data["status_code"] != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_1_default_question(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="What is SeaRates?")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_2_default_question(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="How does SeaRates work?")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_3_default_question(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="Who is a DFA member?")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_4_default_question(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="Who is a carrier?")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_5_default_question(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="Who is a vendor?")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_6_default_question(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="Who is a shipper?")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_le_questions_sea(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="rate 20ft container from new york to washington by sea")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_le_questions_air(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="rate 2000 kg from new york to washington by air")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_le_questions_land(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="rate 200 kg from new york to washington by land")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_ai_send_query_ct_by_cn_query(self, api_client):
        ai_api = api_client(AIApi)
        response = ai_api.post_ai_query(query="find my container CSNU6393245")
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_parce_from_joom(self, api_client):
        parcel_api = api_client(ParcelApi)
        response = parcel_api.get_parcel_info( number="JM000000001327778NPG", carrier_code="JOOM", path= True)
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_parce_from_cnao(self, api_client):
        parcel_api = api_client(ParcelApi)
        response = parcel_api.get_parcel_info( number="AENM0021834400", carrier_code="CNAO", path= False)
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"

    def test_parce_company_info(self, api_client):
        parcel_api = api_client(ParcelApi)
        response = parcel_api.get_parcel_companie_info()
        data = response.json()
        assert response.status_code == 200
        assert data.get("status_code") != "error", f"Unexpected error: {data.get('message')}"



