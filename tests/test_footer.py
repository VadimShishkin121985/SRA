import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.menu_pages.menu_tools import MenuTools
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.footer_page import MenuFooter

@pytest.mark.browser_scope('function')
@pytest.mark.usefixtures('chrome')
class TestFooter:
    _class_cleanup = False  # Флаг для закрытия браузера в конце класса

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

    def test_footer_logistic_explorer(self):
        self.page_footer.go_to_logistic_explorer_from_footer()

    def test_footer_container_tracking(self):
        self.page_footer.go_to_container_tracking_from_footer()

    def test_footer_air_tracking(self):
        self.page_footer.go_to_air_tracking_from_footer()

    def test_footer_ship_schedules(self):
        self.page_footer.go_to_ship_schedules_from_footer()

    def test_footer_logistics_map(self):
        self.page_footer.go_to_logistic_map_from_footer()

    def test_footer_distance_time(self):
        self.page_footer.go_to_distance_and_time_from_footer()

    def test_footer_load_calculator(self):
        self.page_footer.go_to_load_calculator_from_footer()

    def test_footer_freight_index(self):
        self.page_footer.go_to_freight_index_from_footer()

    def test_footer_route_planner(self):
        self.page_footer.go_to_route_planer_from_footer()

    def test_footer_co2_calculator(self):
        self.page_footer.go_to_co2_calculator_from_footer()

    def test_footer_corporate_products(self):
        self.page_footer.go_to_corporates_products_from_footer()



    def test_footer_for_shippers(self):
        self.page_footer.go_to_shippers_from_footer()

    def test_footer_for_carriers(self):
        self.page_footer.go_to_carriers_from_footer()

    def test_footer_integrations(self):
        self.page_footer.go_to_integrations_from_footer()

    def test_footer_find_a_tool(self):
        self.page_footer.go_to_find_a_tool_from_footer()

    def test_footer_developer_portal(self):
        self.page_footer.go_to_developer_portal_from_footer()

    def test_footer_request_an_it_quote(self):
        self.page_footer.go_to_request_it_tool_from_footer()

    def test_footer_affiliates(self):
        self.page_footer.go_to_affiliates_from_page()




    def test_footer_find_freight_route(self):
        self.page_footer.go_to_find_freight_routes_from_footer()

    def test_footer_shipping_line_directory(self):
        self.page_footer.go_to_shipping_lines_directory_from_footer()

    def test_footer_maritime(self):
        self.page_footer.go_to_maritime_from_footer()




    def test_footer_terms_of_service(self):
        self.page_footer.go_to_terms_from_footer()

    def test_footer_privacy_policy(self):
        self.page_footer.go_to_privacy_policy()

    def test_footer_copyright(self):
        self.page_footer.go_to_copyright_from_footer()

    def test_footer_documents_templates(self):
        self.page_footer.go_to_documents_template()




    def test_footer_contact_us(self):
        self.page_footer.go_to_contact_us_from_footer()

    def test_footer_blog(self):
        self.page_footer.go_to_blog_from_footer()

    def test_footer_careers(self):
        self.page_footer.go_to_careers_from_footer()

    def test_footer_help(self):
     self.page_footer.go_to_help_from_footer()

    @classmethod
    def teardown_class(cls):
        cls._class_cleanup = True  # Устанавливаем флаг для закрытия браузера
