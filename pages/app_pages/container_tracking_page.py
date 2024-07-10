import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_page import BasePage


class ContainerTracking(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def searching_by_container_number(self):
        container_number = ['BSIU8174958', 'SLSU8030851', 'CAAU5832492', 'MNBU3710777', 'TRIU6635716', 'EGHU3839887']
        random_container = random.choice(container_number)
        shadow_host = self.driver.find_element(By.ID, 'tracking_system_root')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        #second_shadow_host = self.driver.find_element(By.ID, '.placeholder')
        #second_shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', second_shadow_host)
        teg = shadow_root.find_element(By.CSS_SELECTOR, '.div.OmkQdK:contains("dfdhdhdfhdhdhdhd")')
        #search_input.click()
        teg.click()

        time.sleep(10)

    def searching_by_bl(self):
        bl_number = ['ONEYOS3NA1938600', 'HLCUSZX2310BJOG3', 'MXO0665206', '234234393', 'COSU6370544900', 'EPIRKRFGCL239247', '530300097951']
        random_bl_number = random.choice(bl_number)
        shadow_host = self.driver.find_element(By.ID, 'tracking_system_root')
        shadow_root = self.driver.execute_script('return arguments[0]. shadowRoot', shadow_host)



