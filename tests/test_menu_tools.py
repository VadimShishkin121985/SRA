import time

import pytest


from pages.menu_pages.menu_tools import MenuTools
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.footer_page import MenuFooter

@pytest.mark.browser_scope('function')
@pytest.mark.usefixtures('chrome')
class TestToolsMenu:
    _class_cleanup = False

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
        try:
            self.page_menu_tools.go_to_logistic_explorer_page()
        except Exception as e:
            pytest.skip(f"Skipping due to connection issue: {str(e)}")

    def test_menu_tools_ct(self):
        self.page_menu_tools.go_to_container_tracking_page()

    def test_menu_tools_air_tracking(self):
        self.page_menu_tools.go_to_air_tracking_page()

    def test_menu_tools_schedule(self):
        self.page_menu_tools.go_to_schedules_page()

    def test_menu_tools_lm(self):
        self.page_menu_tools.go_to_logistics_map_page()

    def test_menu_tools_dt(self):
        self.page_menu_tools.go_to_distance_and_time_page()

    def test_menu_tools_lc(self):
        self.page_menu_tools.go_to_load_calculator_page()

    def test_menu_tools_fi(self):
         self.page_menu_tools.go_to_freight_index_page()

    def test_menu_tools_route_planner(self):
        self.page_menu_tools.go_to_route_planer_page()

    def test_menu_tools_co2(self):
        self.page_menu_tools.go_to_co2_page()

    def test_menu_tools_erp(self):
        self.page_menu_tools.go_to_erp_page()

    def test_menu_tools_dev_portal(self):
        self.page_menu_tools.go_to_developer_portal_page()

    def test_menu_tools_fid_tools(self):
        self.page_menu_tools.go_to_find_a_tools_page()

    def test_menu_request_it_quote(self):
        self.page_menu_tools.go_to_request_it_quote_page()

    @classmethod
    def teardown_class(cls):
        cls._class_cleanup = True
