from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import sign_in_page
import time

from pages.app_pages import container_tracking_page
from tests.base_page import BasePage


class MainPage(BasePage):
    _instance = None
    URL = 'https://www.searates.com/'

    def open(self) -> 'MainPage':
        self.driver.get(self.URL)
        return self

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.sign_in_locator = (By.XPATH, '//a[@class="navbar__link navbar__link_signIn | js-nav-item"]')
        self.profile_dropdown_locator = \
            (By.XPATH, '//a[contains(@class,"navbarDropdown__button navbarDropdown__button_profile")]')
        self.profile_name_locator = (By.XPATH, '//span[@class="navbarDropdown__profile-name"]')
        self.container_tracking_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//h4[@class="dropMenu__title"][normalize-space()="Container Tracking"]')
        self.main_logo_locator = (By.XPATH, '')



    def go_to_sign_in_page(self) -> sign_in_page:
        self.driver.find_element(*self.sign_in_locator).click()

    def go_to_container_tracking_app(self) -> container_tracking_page:
        self.driver.find_element(*self.container_tracking_locator).click()

    def verify_login(self):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//a[contains(@class,"navbarDropdown__button navbarDropdown__button_profile")]')))
        element.click()
        assert 'Hi,' in self.driver.find_element(*self.profile_name_locator).text
        time.sleep(1)

    def request_qute(self):
        shadow_host = self.driver.find_element(By.ID, 'main-filter')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        request_a_quote_button = shadow_root.find_element(By.CSS_SELECTOR, '._3IsDO-NbSjzz9KFJTdMj1e')
        request_a_quote_button.click()
        pass

    def tracking_field_search_in_filter(self):
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located(
        #     (By.XPATH, '//div[@class="main__filter | filter"]')))
        #self.privacy_setting()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 30)  # Увеличьте время ожидания до 30 секунд
        shadow_host = wait.until(EC.presence_of_element_located((By.ID, 'main-filter')))
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        tracking_button = shadow_root.find_element(By.CSS_SELECTOR, '.tab-tracking')
        wait.until(EC.element_to_be_clickable(tracking_button))
        tracking_button.click()
        time.sleep(2)


        # shadow_host = self.driver.find_element(By.ID, 'main-filter')
        # shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        # tracking_button = shadow_root.find_element(By.CSS_SELECTOR, '#tab-tracking')
        # tracking_button.click()

    def fill_tracking_field_in_filter_on_main_page(self):
        track_number = 'CAAU5832492'
        shadow_host = self.driver.find_element(By.ID, 'main-filter')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        input_field = shadow_root.find_element(By.CSS_SELECTOR, '.yAW1dd5veYN-0I1dWuR1p')
        input_field.send_keys(track_number)
        time.sleep(2)

    def click_search_button(self):
        shadow_host = self.driver.find_element(By.ID, 'main-filter')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        search_button = shadow_root.find_element(By.CSS_SELECTOR, '.Ye33ELP2gMIzctRlvgbjN')
        time.sleep(5)
        search_button.click()
        shadow_host = self.driver.find_element(By.ID, 'tracking_system_root')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'tracking_system_root')))
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        route_on_the_map = WebDriverWait(shadow_root, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.leaflet-zoom-animated')))
        time.sleep(3)
        assert route_on_the_map.is_displayed(), "Элемент не найден на странице"




