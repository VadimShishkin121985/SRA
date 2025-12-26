

import pytest


from pages.menu_pages.menu_tools import MenuTools
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.footer_page import MenuFooter

@pytest.mark.browser_scope('function')
@pytest.mark.usefixtures('chrome')
class TestServicesMenu:
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

    def test_menu_services_request_quote(self):
        self.page_menu_services.go_to_request_a_quote_page()

    def test_menu_services_active_shipping_leads(self):
        self.page_menu_services.go_to_all_shipping_leads_page()

    def test_menu_services_logistic_service_by_country(self):
        self.page_menu_services.go_to_logistics_services_page()

    def test_menu_services_for_carrier_forwarder_page(self):
        self.page_menu_services.go_to_carrier_forwarder_page()

    def test_menu_services_for_importers_exporters(self):
        self.page_menu_services.go_to_importers_page()

    def test_menu_services_fcl_shipping(self):
        self.page_menu_services.go_to_fcl_shipping_services_page()

    def test_menu_services_lcl_shipping(self):
        self.page_menu_services.go_to_lcl_shipping_services_page()

    def test_menu_services_bulk_and_break_bulk(self):
        self.page_menu_services.go_to_bulk_services_page()

    def test_menu_services_dangerous_cargoes(self):
        self.page_menu_services.go_to_dangerous_cargoes_services_page()

    def test_menu_services_insurance(self):
        self.page_menu_services.go_to_insurance_services_page()

    def test_menu_services_inspection_services(self):
        self.page_menu_services.go_to_inspection_services_page()

    def test_menu_services_abandoned_cargoes(self):
        self.page_menu_services.go_to_abandoned_cargoes_page()

    def test_menu_services_certification(self):
        self.page_menu_services.go_to_certification_services_page()

    def test_menu_services_project_cargo(self):
        self.page_menu_services.go_to_project_cargo_services_page()

    def test_menu_services_customs_clearance_services(self):
        self.page_menu_services.go_to_customs_clearance_services_page()

    def test_menu_services_survey_services(self):
        self.page_menu_services.go_to_survey_services_page()

    def test_menu_services_reefer_services(self):
        self.page_menu_services.go_to_reefer_services_page()

    def test_menu_services_warehousing_services(self):
        self.page_menu_services.go_to_warehousing_services_page()

    def test_menu_services_10_foot_containers(self):
        self.page_menu_services.go_to_test_10_foot_containers_page()

    def test_menu_services_world_sea_ports(self):
        self.page_menu_references.go_to_world_sea_ports_page()

    def test_menu_services_pharmaceutical_healthcare_logistics(self):
        self.page_menu_services.go_to_pharmaceutical_logistics_page()

    def test_menu_services_vehicle_automotive_shipping(self):
        self.page_menu_services.go_to_vehicle_automotive_shipping()

    @classmethod
    def teardown_class(cls):
        cls._class_cleanup = True
