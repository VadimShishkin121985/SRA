import pytest

from selenium.webdriver.common.by import By

from pages.app_pages.container_tracking_page import ContainerTracking
from pages.main_page import MainPage
from pages.menu_pages.menu_tools import MenuTools
from pages.sign_in_page import SignIn


@pytest.mark.usefixtures('chrome')
class Tests:
    _class_cleanup = False  # Флаг для закрытия браузера в конце класса

    @property
    def main_page(self):
        if not hasattr(self, '_main_page'):
            self._main_page = MainPage(self.driver).open()
        return self._main_page

    def test_tracking_from_main_page(self):
        self.main_page.fill_tracking_field_in_filter_on_main_page()




