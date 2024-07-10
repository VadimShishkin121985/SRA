import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import random
import string

from tests.base_page import BasePage


class SignUp(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.email = None
        self.driver: WebDriver = driver
        self.first_name_locator = (By.XPATH, '//input[@id="f_name"]')
        self.last_name_locator = (By.XPATH, '//input[@id="l_name"]')
        self.e_mail_locator = (By.XPATH, '//input[@id="email"]')
        self.phone_number_locator = (By.XPATH, '//input[@name="phone"]')
        self.company_name_locator = (By.XPATH, '//input[@id="company_name"]')
        self.pass_locator = (By.XPATH, '//input[@id="password"]')
        self.button_create_account_locator = (By.XPATH, '//button[@class="L6xZMB yo9FdR"]')

    def fill_sign_up_form(self):

        first_name = 'Something'
        last_name = 'New'
        phone = 67781582
        company_name = 'Test'
        password = 'Test!123'
        self.driver.find_element(*self.first_name_locator).send_keys(first_name)
        self.driver.find_element(*self.last_name_locator).send_keys(last_name)
        self.driver.find_element(*self.e_mail_locator).send_keys(generate_random_email())
        self.driver.find_element(*self.phone_number_locator).send_keys(phone)
        self.driver.find_element(*self.company_name_locator).send_keys(company_name)
        self.driver.find_element(*self.pass_locator).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.button_create_account_locator).click()
        pass

def generate_random_email():
    prefix = "121985ops+"
    suffix = "@gmail.com"

    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    email = f"{prefix}{random_part}{suffix}"

    return email




