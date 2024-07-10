from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages import main_page
from tests.base_page import BasePage


class SignIn(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.login_locator = (By.XPATH, '//input[@type="text"]')
        self.password_locator = (By.XPATH, '//input[@type="password"]')
        self.sign_in_button_locator = (By.XPATH, '//button[@class="L6xZMB yo9FdR"]')
        self.sign_up_locator = (By.XPATH, '//span[@class="RMOtF5"]')

    def sign_in(self) -> main_page:
        email = '121985ops@gmail.com'
        password = 'Acpt!123'
        self.driver.find_element(*self.login_locator).send_keys(email)
        self.driver.find_element(*self.password_locator).send_keys(password)
        self.driver.find_element(*self.sign_in_button_locator).click()

    def go_to_sign_up_page(self):
        self.driver.find_element(*self.sign_up_locator).click()
        pass





