import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_page import BasePage


class LogisticExplorer(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.input_from_locator = (By.ID, 'from')
        self.choose_city_from_autocomplit_locator = (By.XPATH, '//span[text()="Ukraine"]')
        self.choose_port_from_autocomplit_locator = (By.XPATH, '//span[text()="Odesa"]')
        self.input_to_locator = (By.ID, 'to')
        self.choose_city_to_autocomplit_locator = (By.XPATH, '//span[text()="Shanghai, CN"]')
        self.choose_port_to_autocomplit_locator = (By.XPATH, '//span[text()="Shanghai"]')
        self.search_button_locator = (By.XPATH, '//button[@class="zTDkSCFjS5VtNrkEzKtJ5"]')

    def fill_inputs_port_from(self):
        input_from = 'Odesa'
        self.driver.find_element(*self.input_from_locator).send_keys(input_from)
        time.sleep(2)
        self.driver.find_element(*self.choose_city_from_autocomplit_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.choose_port_from_autocomplit_locator).click()
        pass

    def fill_inputs_port_to(self):
        input_to = 'Shanghai'
        self.driver.find_element(*self.input_to_locator).send_keys(input_to)
        time.sleep(2)
        self.driver.find_element(*self.choose_city_to_autocomplit_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.choose_port_to_autocomplit_locator).click()
        pass

    def button_search(self):
        self.driver.find_element(*self.search_button_locator).click()
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="$"]')))
        assert element is not None, "Элемент не найден на странице"
        pass

