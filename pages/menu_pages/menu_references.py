import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_page import BasePage


class MenuReferences(BasePage):
    _instance = None
    URL = 'https://www.searates.com/'

    def open(self) -> 'MenuReferences':
        self.driver.get(self.URL)
        return self

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.menu_references_locator = (By.XPATH, '//a[@data-dropdown="references"]')
        self.world_sea_ports_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="World sea ports"]')
        self.find_port_by_shipping_line_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Find ports by shipping line"]')
        self.sea_line_explorer_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Sea lines explorer"]')
        self.unit_converter_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Unit converter"]')
        self.demurage_and_storage_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Demurrage & Storage"]')
        self.shipping_lines_directory_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Shipping lines directory"]')
        self.incoterms_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Incoterms"]')
        self.imo_classes_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="IMO classes"]')
        self.reefer_cargo_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Reefer cargo"]')
        self.glossary_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Glossary"]')
        self.liner_terms_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Liner terms"]')
        self.services_and_fee_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Services & fees"]')
        self.alpha_scac_codes_locator =(By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Alpha (SCAC) codes"]')
        self.package_type_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Package types"]')
        self.hs_codes_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="HS Codes"]')
        self.container_dimensions_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Container dimensions"]')
        self.palet_dimensions_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Pallet dimensions"]')
        self.uld_container_type = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="ULD container types"]')
        self.type_of_railway_container_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Types of railway wagons"]')
        self.vessel_types_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Shipping lines directory"]')
        self.truck_types_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Truck types"]')

    def move_mouse_to_references(self):
        self.privacy_setting()
        wait = WebDriverWait(self.driver, 50)
        menu_references = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-dropdown="references"]')))
        wait.until(EC.visibility_of(menu_references))
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_references).perform()
        time.sleep(2)

    def waiter_with_assert(self, selector):
        wait = WebDriverWait(self.driver, 50)
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element = wait.until(EC.visibility_of(element))
        assert element is not None, "Элемент не найден"

    def go_to_world_sea_ports_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.world_sea_ports_locator).click()
        self.waiter_with_assert('.requestAQuote-btn')

    def go_to_find_ports_by_shipping_line(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.find_port_by_shipping_line_locator).click()
        self.waiter_with_assert('.page-heading')

    def go_to_demurrage_and_storage(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.demurage_and_storage_locator).click()
        self.waiter_with_assert('.button-center')

    def go_to_sea_lines_explorer_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.sea_line_explorer_locator).click()
        time.sleep(5)
        self.waiter_with_assert('.w-tracking')

    def go_to_unit_converter_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.unit_converter_locator).click()
        self.waiter_with_assert('.reference-block')

    def go_to_shipping_lines_directory(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.shipping_lines_directory_locator).click()
        self.waiter_with_assert('.shipping__list-title')

    def go_to_incoterms_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.incoterms_locator).click()
        self.waiter_with_assert('.incoterms-diagram__nav')

    def go_to_imo_classes_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.imo_classes_locator).click()
        self.waiter_with_assert('.imo-block')

    def go_to_reefer_cargo_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.reefer_cargo_locator).click()
        self.waiter_with_assert('.filtr-box')

    def go_to_glossary_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.glossary_locator).click()
        self.waiter_with_assert('.glossary-terms__description')

    def go_to_liner_terms_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.liner_terms_locator).click()
        self.waiter_with_assert('.page-heading')

    def go_to_services_and_fee_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.services_and_fee_locator).click()
        self.waiter_with_assert('.fees-item__head')

    def go_to_alpha_scac_codes_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.alpha_scac_codes_locator).click()
        self.waiter_with_assert('.alphabet-wrapper')

    def go_to_package_types_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.package_type_locator).click()
        self.waiter_with_assert('.search-text')

    def go_to_hs_codes_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.hs_codes_locator).click()
        time.sleep(3)
        self.waiter_with_assert('.hs-codes__row')

    def go_to_container_dimensions_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.container_dimensions_locator).click()
        self.waiter_with_assert('.equipment-wrapper')

    def go_to_palet_dimensions_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.palet_dimensions_locator).click()
        self.waiter_with_assert('.table__row')

    def go_to_uld_container_type_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.uld_container_type).click()
        self.waiter_with_assert('.equipment-item')

    def go_to_type_of_railway_container_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.type_of_railway_container_locator).click()
        self.waiter_with_assert('.railway-cards-item')

    def go_to_vessel_type_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.vessel_types_locator).click()
        self.waiter_with_assert('.shipping__list-title')

    def go_to_truck_type_page(self):
        self.move_mouse_to_references()
        self.driver.find_element(*self.truck_types_locator).click()
        self.waiter_with_assert('.truck-types__categories')