import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.menu_pages.menu_tools import MenuTools
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.footer_page import MenuFooter

@pytest.mark.usefixtures('chrome')
class TestToolsMenu:
    def setup_method(self, driver):  # Предполагаем, что фикстура driver настроена
        self.driver: WebDriver = self.driver

    def teardown_method(self):
        try:
            if hasattr(self, 'driver'):
                self.driver.quit()
        except Exception as e:
            print(f"Error in teardown: {str(e)}")
        finally:
            # Очищаем ссылки на страницы для следующего теста
            if hasattr(self, '_page_menu_tools'):
                delattr(self, '_page_menu_tools')

    @property
    def page_menu_tools(self):
        if not hasattr(self, '_page_menu_tools'):
            self._page_menu_tools = MenuTools(self.driver).open()
        return self._page_menu_tools

    @property
    def page_menu_services(self):
        if not hasattr(self, '_page_menu_services'):
            self._page_menu_services = MenuServices(self.driver).open()
        return self._page_menu_services

    @property
    def page_menu_references(self):
        if not hasattr(self, '_page_menu_references'):
            self._page_menu_references = MenuReferences(self.driver).open()
        return self._page_menu_references

    @property
    def page_menu_company(self):
        if not hasattr(self, '_page_menu_company'):
            self._page_menu_company = MenuCompany(self.driver).open()
        return self._page_menu_company

    @property
    def page_footer(self):
        if not hasattr(self, '_page_footer'):
            self._page_footer = MenuFooter(self.driver).open()
        return self._page_footer

    def test_menu_tools_le(self):
        self.page_menu_tools.go_to_logistic_explorer_page()


    def test_menu_tools_ct(self):
        self.page_menu_tools.go_to_container_tracking_page()
        time.sleep(2)

    def test_menu_tools_air_tracking(self):
        self.page_menu_tools.go_to_air_tracking_page()

    # def test_menu_tools_schedule(self):
    #     self.page_menu_tools.go_to_schedules_page()
    #
    # def test_menu_tools_lm(self):
    #     self.page_menu_tools.go_to_logistics_map_page()
    #
    # def test_menu_tools_dt(self):
    #     self.page_menu_tools.go_to_distance_and_time_page()
    #
    # def test_menu_tools_lc(self):
    #     self.page_menu_tools.go_to_load_calculator_page()
    #
    # def test_menu_tools_fi(self):
    #     self.page_menu_tools.go_to_freight_index_page()
    #
    # def test_menu_tools_route_planner(self):
    #     self.page_menu_tools.go_to_route_planer_page()
    #
    # def test_menu_tools_co2(self):
    #     self.page_menu_tools.go_to_co2_page()
    #
    # def test_menu_tools_erp(self):
    #     self.page_menu_tools.go_to_erp_page()
    #
    # def test_menu_tools_searates_exp(self):
    #     self.page_menu_tools.go_to_se_page()
    #
    # def test_menu_tools_dev_portal(self):
    #     self.page_menu_tools.go_to_developer_portal_page()
    #
    # def test_menu_tools_fid_tools(self):
    #     self.page_menu_tools.go_to_find_a_tools_page()
    #
    # def test_menu_request_it_quote(self):
    #     self.page_menu_tools.go_to_request_it_quote_page()
    #
    # def test_menu_services_request_quote(self):
    #     self.page_menu_services.go_to_request_a_quote_page()
    #
    # def test_menu_services_active_shipping_leads(self):
    #     self.page_menu_services.go_to_all_shipping_leads_page()
    #
    # def test_menu_services_logistic_service_by_country(self):
    #     self.page_menu_services.go_to_logistics_services_page()
    #
    # def test_for_carrier_forwarder_page(self):
    #     self.page_menu_services.go_to_carrier_forwarder_page()
    #
    # def test_for_importers_exporters(self):
    #     self.page_menu_services.go_to_importers_page()
    #
    # def test_fcl_shipping(self):
    #     self.page_menu_services.go_to_fcl_shipping_services_page()
    #
    # def test_lcl_shipping(self):
    #     self.page_menu_services.go_to_lcl_shipping_services_page()
    #
    # def test_bulk_and_break_bulk(self):
    #     self.page_menu_services.go_to_bulk_services_page()
    #
    # def test_dangerous_cargoes(self):
    #     self.page_menu_services.go_to_dangerous_cargoes_services_page()
    #
    # def test_insurance(self):
    #     self.page_menu_services.go_to_insurance_services_page()
    #
    # def test_inspection_services(self):
    #     self.page_menu_services.go_to_inspection_services_page()
    #
    # def test_abandoned_cargoes(self):
    #     self.page_menu_services.go_to_abandoned_cargoes_page()
    #
    # def test_certification(self):
    #     self.page_menu_services.go_to_certification_services_page()
    #
    # def test_project_cargo(self):
    #     self.page_menu_services.go_to_project_cargo_services_page()
    #
    # def test_customs_clearance_services(self):
    #     self.page_menu_services.go_to_customs_clearance_services_page()
    #
    # def test_survey_services(self):
    #     self.page_menu_services.go_to_survey_services_page()
    #
    # def test_reefer_services(self):
    #     self.page_menu_services.go_to_reefer_services_page()
    #
    # def test_warehousing_services(self):
    #     self.page_menu_services.go_to_warehousing_services_page()
    #
    # def test_10_foot_containers(self):
    #     self.page_menu_services.go_to_test_10_foot_containers_page()
    #
    # def test_world_sea_ports(self):
    #     self.page_menu_references.go_to_world_sea_ports_page()
    #
    # def test_find_ports_by_shipping_line(self):
    #     self.page_menu_references.go_to_find_ports_by_shipping_line()
    #
    # def test_demurrage_and_storage(self):
    #     self.page_menu_references.go_to_demurrage_and_storage()
    #
    # def test_sea_lines_explorer(self):
    #     self.page_menu_references.go_to_sea_lines_explorer_page()
    #
    # def test_shipping_lines_directory(self):
    #     self.page_menu_references.go_to_shipping_lines_directory()
    #
    # def test_unit_converter(self):
    #     self.page_menu_references.go_to_unit_converter_page()
    #
    # def test_incoterms(self):
    #     self.page_menu_references.go_to_incoterms_page()
    #
    # def test_imo_classes(self):
    #     self.page_menu_references.go_to_imo_classes_page()
    #
    # def test_reefer_cargo(self):
    #     self.page_menu_references.go_to_reefer_cargo_page()
    #
    # def test_glossary(self):
    #     self.page_menu_references.go_to_glossary_page()
    #
    # def test_liner_terms(self):
    #     self.page_menu_references.go_to_liner_terms_page()
    #
    # def test_services_and_fee(self):
    #     self.page_menu_references.go_to_services_and_fee_page()
    #
    # def test_alpha_scac_codes(self):
    #     self.page_menu_references.go_to_alpha_scac_codes_page()
    #
    # def test_package_types(self):
    #     self.page_menu_references.go_to_package_types_page()
    #
    # def test_hs_codes(self):
    #     self.page_menu_references.go_to_hs_codes_page()
    #
    # def test_container_dimensions(self):
    #     self.page_menu_references.go_to_container_dimensions_page()
    #
    # def test_palet_dimensions(self):
    #     self.page_menu_references.go_to_palet_dimensions_page()
    #
    # def test_uld_container_type(self):
    #     self.page_menu_references.go_to_uld_container_type_page()
    #
    # def test_type_of_railway_container(self):
    #     self.page_menu_references.go_to_type_of_railway_container_page()
    #
    # def test_vessel_type(self):
    #     self.page_menu_references.go_to_vessel_type_page()
    #
    # def test_truck_type(self):
    #     self.page_menu_references.go_to_truck_type_page()
    #
    # def test_contact_us(self):
    #     self.page_menu_company.go_to_contact_us_page()
    #
    # def test_about_us(self):
    #     self.page_menu_company.go_to_about_us_page()
    #
    # def test_faqs(self):
    #     self.page_menu_company.go_to_faqs_page()
    #
    # def test_blog(self):
    #     self.page_menu_company.go_to_blog_page()
    #
    # def test_blog_post(self):
    #     self.page_menu_company.go_to_blog_post()
    #
    # def test_footer_logistic_explorer(self):
    #     self.page_footer.go_to_logistic_explorer_from_footer()
    #
    # def test_footer_container_tracking(self):
    #     self.page_footer.go_to_container_tracking_from_footer()
    #
    # def test_footer_air_tracking(self):
    #     self.page_footer.go_to_air_tracking_from_footer()
    #
    # def test_footer_ship_schedules(self):
    #     self.page_footer.go_to_ship_schedules_from_footer()
    #
    # def test_footer_logistics_map(self):
    #     self.page_footer.go_to_logistic_map_from_footer()
    #
    # def test_footer_distance_time(self):
    #     self.page_footer.go_to_distance_and_time_from_footer()
    #
    # def test_footer_load_calculator(self):
    #     self.page_footer.go_to_load_calculator_from_footer()
    #
    # def test_footer_freight_index(self):
    #     self.page_footer.go_to_freight_index_from_footer()
    #
    # def test_footer_route_planner(self):
    #     self.page_footer.go_to_route_planer_from_footer()
    #
    # def test_footer_co2_calculator(self):
    #     self.page_footer.go_to_co2_calculator_from_footer()
    #
    # def test_footer_for_shippers(self):
    #     self.page_footer.go_to_shippers_from_footer()
    #
    # def test_footer_for_carriers(self):
    #     self.page_footer.go_to_carriers_from_footer()
    #
    # def test_footer_integrations(self):
    #     self.page_footer.go_to_integrations_from_footer()
    #
    # def test_footer_find_a_tool(self):
    #     self.page_footer.go_to_find_a_tool_from_footer()
    #
    # def test_footer_developer_portal(self):
    #     self.page_footer.go_to_developer_portal_from_footer()
    #
    # def test_footer_request_an_it_quote(self):
    #     self.page_footer.go_to_request_it_tool_from_footer()
    #
    # def test_footer_affiliates(self):
    #     self.page_footer.go_to_affiliates_from_page()
    #
    # def test_footer_find_freight_route(self):
    #     self.page_footer.go_to_find_freight_routes_from_footer()
    #
    # def test_footer_shipping_line_directory(self):
    #     self.page_footer.go_to_shipping_lines_directory_from_footer()
    #
    # def test_footer_maritime(self):
    #     self.page_footer.go_to_maritime_from_footer()
    #
    # def test_footer_terms_of_service(self):
    #     self.page_footer.go_to_terms_from_footer()
    #
    # def test_footer_privacy_policy(self):
    #     self.page_footer.go_to_privacy_policy()
    #
    # def test_footer_copyright(self):
    #     self.page_footer.go_to_copyright_from_footer()
    #
    # def test_footer_documents_templates(self):
    #     self.page_footer.go_to_documents_template()
    #
    # def test_footer_contact_us(self):
    #     self.page_footer.go_to_contact_us_from_footer()
    #
    # def test_footer_blog(self):
    #     self.page_footer.go_to_blog_from_footer()
    #
    # def test_footer_careers(self):
    #     self.page_footer.go_to_careers_from_footer()
    #
    # def test_footer_help(self):
    #  self.page_footer.go_to_help_from_footer()
