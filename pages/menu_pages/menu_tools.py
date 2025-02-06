from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from tests.base_page import BasePage


class MenuTools(BasePage):
    _instance = None
    URL = 'https://www.searates.com/'

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.sign_in_locator = (By.XPATH, '//a[@class="navbar__link navbar__link_signIn | js-nav-item"]')
        self.profile_dropdown_locator = (By.XPATH, '//a[contains(@class,"navbarDropdown__button navbarDropdown__button_profile")]')
        self.profile_name_locator = (By.XPATH, '//span[@class="navbarDropdown__profile-name"]')
        self.logistic_explorer_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__title"][normalize-space()="Logistics Explorer"]')
        self.container_tracking_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][normalize-space()="See your cargo location on the map in real-time"]')
        self.ship_schedules_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][contains(text(),"Find sailing schedules by route or vessel with mul")]')
        self.air_tracking_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][normalize-space()="Track your air cargoes by airwaybill number"]')
        self.load_calculator_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][normalize-space()="The smart engine for transport stuffing"]')
        self.logistics_map_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][contains(text(),"Interactive map for freight requests, transport an")]')
        self.distance_and_time_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][contains(text(),"Visual module with map, showing sea and land routi")]')
        self.route_planer_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][normalize-space()="A tool for carriers to provide accurate tracking"]')
        self.erp_page_locator =(By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][contains(text(),"A highly cost effective and fully integrated ERP S")]')
        self.dev_portal_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Developer portal"]')
        self.element_devportal_locator = (By.XPATH, '//h1[@class="text-center h-text-gradient"]')
        self.freight_index_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][contains(text(),"Freight analytics tool with historical data for se")]')
        self.menu_tools_locator = (By.XPATH, '//a[@data-dropdown="tools"]')
        self.find_tols_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//a[@class="dropMenu__link dropMenu__link dropMenu__link_size-16 dropMenu__link_mr-15 find-tool-btn"][normalize-space()="Find a tool"]')
        self.assert_element_find_from_tols_page_locator = (By.XPATH, '//a[@class="button pricing"]')
        self.request_it_qoute_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Request an IT quote"]')
        self.carbon_emition_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__title-text"][normalize-space()="CO2 Calculator"]')
        self.searates_expres_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//p[@class="dropMenu__subtitle dropMenu__subtitle-visible"][normalize-space()="Efficient solution for Freight Forwarders"]')


    def open(self) -> 'MenuTools':
        self.driver.get(self.URL)
        return self

    def move_mouse_to_tools(self):
        self.privacy_setting()
        menu_tools = self.driver.find_element(By.XPATH, '//a[@data-dropdown="tools"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_tools).perform()
        time.sleep(2)

    def go_to_container_tracking_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.container_tracking_locator).click()
        self.waiter_with_assert('#tracking_system_root')

    def waiter_with_assert(self, selector):
        wait = WebDriverWait(self.driver, 50)
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        element = wait.until(element_present)
        assert element is not None, "Элемент не найден"

    def go_to_logistic_explorer_page(self):
        self.move_mouse_to_tools()
        time.sleep(10)
        self.driver.find_element(*self.logistic_explorer_locator).click()
        self.waiter_with_assert('#shadow-wrapper-le')
        pass

    def go_to_schedules_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.ship_schedules_locator).click()
        self.waiter_with_assert('.FrpaIW')

    def go_to_air_tracking_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.air_tracking_locator).click()
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1)
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        self.waiter_with_assert('#tracking_system_root')
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def go_to_load_calculator_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.load_calculator_locator).click()
        self.waiter_with_assert('#loadCalculator')
        self.driver.back()

    def go_to_logistics_map_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.logistics_map_locator).click()
        time.sleep(5)
        self.waiter_with_assert('.logistics-map-HpouLQ')

    def go_to_distance_and_time_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.distance_and_time_locator).click()
        wait = WebDriverWait(self.driver, 50)
        text_on_distans_and_time_page = (By.XPATH, '//p[contains(text(), "Select port (place)")]')
        element_with_text = wait.until(EC.visibility_of_element_located(text_on_distans_and_time_page))
        text = element_with_text.text
        time.sleep(3)
        #expected_text = 'Select port (place) of origin and port (place) of destination, then time interval for your schedule and hit Search button.'
        #assert expected_text == text, f"Текст '{expected_text}' не соответствует полученому тексту '{text}'"

    def go_to_route_planer_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.route_planer_locator).click()
        self.waiter_with_assert('.ro-project')

    def go_to_erp_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.erp_page_locator).click()
        self.waiter_with_assert('.subtitle')

    def go_to_se_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.searates_expres_locator).click()
        self.waiter_with_assert('.btn-box')

    def go_to_freight_index_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.freight_index_locator).click()
        self.waiter_with_assert('.gOsv4N')

    def go_to_developer_portal_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.dev_portal_locator).click()
        self.waiter_with_assert('.text-center')
        self.driver.back()

    def go_to_find_a_tools_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.find_tols_locator).click()
        self.waiter_with_assert('.tool-box')

    def go_to_request_it_quote_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.request_it_qoute_locator).click()
        self.waiter_with_assert('.jzUXQV')

    def go_to_co2_page(self):
        self.move_mouse_to_tools()
        self.driver.find_element(*self.carbon_emition_locator).click()
        self.waiter_with_assert('#carbon-emissions-calculator-root')

