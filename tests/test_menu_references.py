import pytest

from pages.menu_pages.menu_tools import MenuTools
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.footer_page import MenuFooter


@pytest.mark.browser_scope('function')
@pytest.mark.usefixtures('chrome')
class TestMenu:
    _class_cleanup = False

    # =========================================================
    # 🔧 PAGE OBJECTS (lazy init)
    # =========================================================
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

    # =========================================================
    # 📚 REFERENCES
    # =========================================================
    def test_references_world_sea_ports(self):
        self.page_menu_references.go_to_world_sea_ports_page()

    def test_references_demurrage_and_storage(self):
        self.page_menu_references.go_to_demurrage_and_storage()

    def test_references_unit_converter(self):
        self.page_menu_references.go_to_unit_converter_page()

    def test_references_carrier_directory(self):
        self.page_menu_references.go_to_carrier_directory_page()

    def test_references_incoterms(self):
        self.page_menu_references.go_to_incoterms_page()

    def test_references_imo_classes(self):
        self.page_menu_references.go_to_imo_classes_page()

    def test_references_reefer_cargo(self):
        self.page_menu_references.go_to_reefer_cargo_page()

    def test_references_glossary(self):
        self.page_menu_references.go_to_glossary_page()

    def test_references_liner_terms(self):
        self.page_menu_references.go_to_liner_terms_page()

    def test_references_services_and_fee(self):
        self.page_menu_references.go_to_services_and_fee_page()

    def test_references_alpha_scac_codes(self):
        self.page_menu_references.go_to_alpha_scac_codes_page()

    def test_references_package_types(self):
        self.page_menu_references.go_to_package_types_page()

    def test_references_hs_codes(self):
        self.page_menu_references.go_to_hs_codes_page()

    def test_references_find_ports_by_shipping_line(self):
        self.page_menu_references.go_to_find_ports_by_shipping_line()

    def test_references_sea_lines_explorer(self):
        self.page_menu_references.go_to_sea_lines_explorer_page()

    def test_references_shipping_lines_directory(self):
        self.page_menu_references.go_to_shipping_lines_directory()

    def test_references_container_dimensions(self):
        self.page_menu_references.go_to_container_dimensions_page()

    def test_references_palet_dimensions(self):
        self.page_menu_references.go_to_palet_dimensions_page()

    def test_references_uld_container_type(self):
        self.page_menu_references.go_to_uld_container_type_page()

    def test_references_type_of_railway_container(self):
        self.page_menu_references.go_to_type_of_railway_container_page()

    def test_references_vessel_type(self):
        self.page_menu_references.go_to_vessel_type_page()

    def test_references_truck_type(self):
        self.page_menu_references.go_to_truck_type_page()

    # =========================================================
    # 🚢 SERVICES
    # =========================================================
    def test_services_request_quote(self):
        self.page_menu_services.go_to_request_a_quote_page()

    def test_services_active_shipping_leads(self):
        self.page_menu_services.go_to_all_shipping_leads_page()

    def test_services_logistic_service_by_country(self):
        self.page_menu_services.go_to_logistics_services_page()

    def test_services_for_carrier_forwarder(self):
        self.page_menu_services.go_to_carrier_forwarder_page()

    def test_services_for_importers_exporters(self):
        self.page_menu_services.go_to_importers_page()

    def test_services_fcl_shipping(self):
        self.page_menu_services.go_to_fcl_shipping_services_page()

    def test_services_lcl_shipping(self):
        self.page_menu_services.go_to_lcl_shipping_services_page()

    def test_services_bulk_and_break_bulk(self):
        self.page_menu_services.go_to_bulk_services_page()

    def test_services_dangerous_cargoes(self):
        self.page_menu_services.go_to_dangerous_cargoes_services_page()

    def test_services_insurance(self):
        self.page_menu_services.go_to_insurance_services_page()

    def test_services_inspection_services(self):
        self.page_menu_services.go_to_inspection_services_page()

    def test_services_abandoned_cargoes(self):
        self.page_menu_services.go_to_abandoned_cargoes_page()

    def test_services_certification(self):
        self.page_menu_services.go_to_certification_services_page()

    def test_services_project_cargo(self):
        self.page_menu_services.go_to_project_cargo_services_page()

    def test_services_customs_clearance(self):
        self.page_menu_services.go_to_customs_clearance_services_page()

    def test_services_survey_services(self):
        self.page_menu_services.go_to_survey_services_page()

    def test_services_reefer_services(self):
        self.page_menu_services.go_to_reefer_services_page()

    def test_services_warehousing(self):
        self.page_menu_services.go_to_warehousing_services_page()

    def test_services_10_foot_containers(self):
        self.page_menu_services.go_to_test_10_foot_containers_page()

    def test_services_pharmaceutical_logistics(self):
        self.page_menu_services.go_to_pharmaceutical_logistics_page()

    def test_services_vehicle_automotive(self):
        self.page_menu_services.go_to_vehicle_automotive_shipping()

    # =========================================================
    # 🏢 COMPANY
    # =========================================================
    def test_company_contact_us(self):
        self.page_menu_company.go_to_contact_us_page()

    def test_company_about_us(self):
        self.page_menu_company.go_to_about_us_page()

    def test_company_faqs(self):
        self.page_menu_company.go_to_faqs_page()

    def test_company_blog(self):
        self.page_menu_company.go_to_blog_page()

    def test_company_blog_post(self):
        self.page_menu_company.go_to_blog_post()

    # =========================================================
    # 🧹 CLEANUP
    # =========================================================
    @classmethod
    def teardown_class(cls):
        cls._class_cleanup = True