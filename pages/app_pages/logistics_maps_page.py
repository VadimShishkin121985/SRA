import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_page import BasePage


class LogisticsMaps(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver