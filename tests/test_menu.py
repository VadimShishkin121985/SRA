import traceback

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import time
import allure

from pages import request_a_quote_page
from pages.main_page import MainPage
from pages.menu_pages.footer_page import MenuFooter
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_tools import MenuTools


@allure.epic("SeaRates Tests")
@allure.feature("Menu Navigation")
class Test:
    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_menu_tools = MenuTools(self.driver).open()
        self.main_page = MainPage(self.driver).open

    @allure.story("Quick Actions")
    @allure.title("Quick request button works")
    def test_quick_request_button(self):
        self.main_page.request_qute()

    @allure.story("Tools Menu")
    class TestToolsMenu:
        @allure.title("User can open Logistic Explorer")
        def test_menu_tools_le(self):
            self.page_menu_tools.go_to_logistic_explorer_page()

        @allure.title("User can open Container Tracking")
        def test_menu_tools_ct(self):
            self.page_menu_tools.go_to_container_tracking_page()
            #self.page_menu_tools.go_to_air_tracking_page()
        def test_menu_tools_shdule(self):
            self.page_menu_tools.go_to_schedules_page()

        def test_menu_tools_lm(self):
            self.page_menu_tools.go_to_logistics_map_page()

        def test_menu_tools_dt(self):
            self.page_menu_tools.go_to_distance_and_time_page()

        def test_menu_tools_lc(self):
            self.page_menu_tools.go_to_load_calculator_page()

        #
        # def test_menu_tools_fi(self):
        #     self.page_menu_tools.go_to_freight_index_page()
        #
        # def test_menu_tools_route_plaer(self):
        #     self.page_menu_tools.go_to_route_planer_page()
        #
        # def test_menu_tools_co2(self):
        #     self.page_menu_tools.go_to_co2_page()
        #
        # def test_menu_tools_erp(self):
        #     self.page_menu_tools.go_to_erp_page()
        #
        # def test_menu_tools_dev_portal(self):
        #     self.page_menu_tools.go_to_developer_portal_page()
        #
        # def test_menu_tools_fid_tools(self):
        #     self.page_menu_tools.go_to_find_a_tools_page()
        #
        # def test_menu_request_quote(self):
        #     self.page_menu_tools.go_to_request_it_quote_page()
        #
        #
        # def test_menu_services(self):
        #     self.page_menu_services = MenuServices(self.driver).open()
        #     self.page_menu_services.go_to_request_a_quote_page()
        #     self.page_menu_services.go_to_all_shipping_leads_page()
        #     self.page_menu_services.go_to_logistics_services_page()
        #     self.page_menu_services.go_to_carrier_forwarder_page()
        #     self.page_menu_services.go_to_importers_page()
        #     self.page_menu_services.go_to_fcl_shipping_services_page()
        #     self.page_menu_services.go_to_lcl_shipping_services_page()
        #     self.page_menu_services.go_to_bulk_services_page()
        #     self.page_menu_services.go_to_dangerous_cargoes_services_page()
        #     self.page_menu_services.go_to_insurance_services_page()
        #     self.page_menu_services.go_to_inspection_services_page()
        #     self.page_menu_services.go_to_certification_services_page()
        #     self.page_menu_services.go_to_project_cargo_services_page()
        #     self.page_menu_services.go_to_customs_clearance_services_page()
        #     self.page_menu_services.go_to_survey_services_page()
        #     self.page_menu_services.go_to_reefer_services_page()
        #     self.page_menu_services.go_to_warehousing_services_page()
        #     pass
        #
        # def test_menu_references(self):
        #     self.page_menu_references = MenuReferences(self.driver).open()
        #     self.page_menu_references.go_to_world_sea_ports_page()
        #     self.page_menu_references.go_to_find_ports_by_shipping_line()
        #     self.page_menu_references.go_to_demurrage_and_storage()
        #     self.page_menu_references.go_to_sea_lines_explorer_page()
        #     self.page_menu_references.go_to_unit_converter_page()
        #     self.page_menu_references.go_to_shipping_lines_directory()
        #     self.page_menu_references.go_to_incoterms_page()
        #     self.page_menu_references.go_to_imo_classes_page()
        #     self.page_menu_references.go_to_reefer_cargo_page()
        #     self.page_menu_references.go_to_glossary_page()
        #     self.page_menu_references.go_to_liner_terms_page()
        #     self.page_menu_references.go_to_services_and_fee_page()
        #     self.page_menu_references.go_to_alpha_scac_codes_page()
        #     self.page_menu_references.go_to_package_types_page()
        #     self.page_menu_references.go_to_hs_codes_page()
        #     self.page_menu_references.go_to_container_dimensions_page()
        #     self.page_menu_references.go_to_palet_dimensions_page()
        #     self.page_menu_references.go_to_uld_container_type_page()
        #     self.page_menu_references.go_to_type_of_railway_container_page()
        #     self.page_menu_references.go_to_vessel_type_page()
        #     self.page_menu_references.go_to_truck_type_page()
        #     pass
        #
        # def test_menu_company(self):
        #     self.page_menu_company = MenuCompany(self.driver).open()
        #     self.page_menu_company.go_to_contact_us_page()
        #     self.page_menu_company.go_to_about_us_page()
        #     self.page_menu_company.go_to_faqs_page()
        #     self.page_menu_company.go_to_blog_page()
        #     self.page_menu_company.go_to_blog_post()
        #     time.sleep(5)
        #     pass
        #
        # def test_footer(self):
        #     def safe_call(method):
        #         try:
        #             method()
        #         except Exception as e:
        #             print(f"An error occurred in {method.__name__}: {e}")
        #             traceback.print_exc()
        #
        #     self.page_footer = MenuFooter(self.driver).open()
        #     safe_call(self.page_footer.go_to_logistic_explorer_from_footer)
        #     safe_call(self.page_footer.go_to_container_tracking_from_footer)
        #     safe_call(self.page_footer.go_to_air_tracking_from_footer)
        #     safe_call(self.page_footer.go_to_ship_schedules_from_footer)
        #     safe_call(self.page_footer.go_to_load_calculator_from_footer)
        #     safe_call(self.page_footer.go_to_logistic_map_from_footer)
        #     safe_call(self.page_footer.go_to_distance_and_time_from_footer)
        #     safe_call(self.page_footer.go_to_route_planer_from_footer)
        #     safe_call(self.page_footer.go_to_shippers_from_footer)
        #     safe_call(self.page_footer.go_to_carriers_from_footer)
        #     safe_call(self.page_footer.go_to_integrations_from_footer)
        #     safe_call(self.page_footer.go_to_api_from_footer)
        #     safe_call(self.page_footer.go_to_developer_portal_from_footer)
        #     safe_call(self.page_footer.go_to_request_it_tool_from_footer)
        #     safe_call(self.page_footer.go_to_find_freight_routes_from_footer)
        #     safe_call(self.page_footer.go_to_shipping_lines_directory_from_footer)
        #     safe_call(self.page_footer.go_to_maritime_from_footer)
        #     safe_call(self.page_footer.go_to_terms_from_footer)
        #     safe_call(self.page_footer.go_to_privacy_policy)
        #     safe_call(self.page_footer.go_to_copyright_from_footer)
        #     safe_call(self.page_footer.go_to_documents_template)
        #     safe_call(self.page_footer.go_to_contact_us_from_footer)
        #     safe_call(self.page_footer.go_to_blog_from_footer)
        #     safe_call(self.page_footer.go_to_careers_from_footer)
        #     safe_call(self.page_footer.go_to_help_from_footer)
        #
        # def test_test(self):
        #     self.page_footer = MenuFooter(self.driver).open()
        #     self.page_footer.go_to_documents_template()
        #     time.sleep(10)
