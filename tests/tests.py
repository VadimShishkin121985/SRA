import pytest
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from pages.app_pages.container_tracking_page import ContainerTracking
from pages.main_page import MainPage
from pages.menu_pages.menu_tools import MenuTools
from pages.sign_in_page import SignIn


@pytest.mark.usefixtures('chrome')
class Tests:
    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_main = MainPage(self.driver).open
        #self.service = self._get_gmail_service()

    def test_login(self):
        self.driver.find_element(By.XPATH, '//a[@class="navbar__link navbar__link_signIn | js-nav-item"]')
        self.page_sign_in = SignIn(self.driver)
        self.page_main.go_to_sign_in_page()
        self.page_sign_in.sign_in()
        self.page_main.verify_login()
        pass

    def test_tracking_from_main_page(self):
        self.test_login()
        self.page_main.tracking_field_search_in_filter()
        self.page_main.fill_tracking_field_in_filter_on_main_page()
        self.page_main.click_search_button()

    def test_tracking_search_via_ct(self):
        self.test_login()
        self.page_menu_tools = MenuTools(self.driver)
        self.page_menu_tools.go_to_container_tracking_page()
        self.page_container_tracking = ContainerTracking(self.driver)
        self.page_container_tracking.searching_by_container_number()

    def test_tracking_search_via_bl(self):
        self.test_login()
        self.page_menu_tools.go_to_container_tracking_page()




