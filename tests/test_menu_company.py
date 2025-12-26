

import pytest


from pages.menu_pages.menu_tools import MenuTools
from pages.menu_pages.menu_services import MenuServices
from pages.menu_pages.menu_references import MenuReferences
from pages.menu_pages.menu_company import MenuCompany
from pages.menu_pages.footer_page import MenuFooter

@pytest.mark.browser_scope('function')
@pytest.mark.usefixtures('chrome')
class TestCompanyMenu:
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

    @classmethod
    def teardown_class(cls):
        cls._class_cleanup = True