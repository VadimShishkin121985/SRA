import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_page import BasePage


class MenuServices(BasePage):
    _instance = None
    URL = 'https://www.searates.com/'

    def open(self) -> 'MenuServices':
        self.driver.get(self.URL)
        return self

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.menu_services_locator = (By.XPATH, '//a[@data-dropdown="services"]')
        self.request_a_quote_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__item__request__title"][normalize-space()="Request a quote"]')
        self.all_shipping_leads_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text_icon dropMenu__text-width-225"][normalize-space()="Active shipping leads"]')
        self.logistics_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text_icon dropMenu__text-width-225"][normalize-space()="Logistics services by country"]')
        self.carrier_forwarder_page_locator =(By.XPATH, '//div[@class="dropMenu"]//div[@class="dropMenu__list_block drop-services__link dropMenu__list_flex-block dropMenu__link_max-width-276"]//a[2]//span[1]')
        self.importer_page_locator = (By.XPATH,'//div[@class="dropMenu"]//div[@class="dropMenu__list_block drop-services__link dropMenu__list_flex-block dropMenu__link_max-width-276"]//a[1]//span[1]')
        self.fcl_shipping_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="FCL shipping"]')
        self.lcl_shipping_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="LCL shipping"]')
        self.bulk_shipping_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Bulk & break bulk"]')
        self.dangerous_cargoes_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Dangerous cargoes"]')
        self.insurance_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Insurance"]')
        self.inspection_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Inspection services"]')
        self.certification_service_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Certification"]')
        self.project_cargo_service_page_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Project cargo"]')
        self.custom_clearance_service_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Customs clearance"]')
        self.survey_cervices_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Survey services"]')
        self.reefer_cargoes_cervices_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Reefer cargoes"]')
        self.warehousing_services_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Warehousing"]')
        self.customs_clearance_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Customs clearance"]')
        self.abandoned_cargoes_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="Abandoned cargoes"]')
        self.teen_foot_containers_locator = (By.XPATH, '//div[@class="dropMenu__content drop-services__content js-drop-content"]//span[@class="dropMenu__text"][normalize-space()="10-foot containers"]')

    def move_mouse_to_services(self):
        #self.privacy_setting()
        menu_tools = self.driver.find_element(By.XPATH, '//a[@data-dropdown="services"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_tools).perform()
        time.sleep(2)

    def waiter_with_assert(self, selector):
        wait = WebDriverWait(self.driver, 50)
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element = wait.until(EC.visibility_of(element))
        assert element is not None, "Элемент не найден"

    def go_to_request_a_quote_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.request_a_quote_locator).click()
        self.waiter_with_assert('.eLavM')

    def go_to_all_shipping_leads_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.all_shipping_leads_locator).click()
        time.sleep(8)
        self.waiter_with_assert('._2f40ek0H0uloebYpv4FRdk')

    def go_to_logistics_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.logistics_services_locator).click()
        self.waiter_with_assert('.alphabet')

    def go_to_carrier_forwarder_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.carrier_forwarder_page_locator).click()
        self.waiter_with_assert('.link-wrapper')

    def go_to_importers_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.importer_page_locator).click()
        self.waiter_with_assert('.section-btn.cu_open-form')

    def go_to_fcl_shipping_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.fcl_shipping_services_locator).click()
        self.waiter_with_assert('.intro-picture')

    def go_to_lcl_shipping_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.lcl_shipping_services_locator).click()
        self.waiter_with_assert('.btn-intro')

    def go_to_bulk_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.bulk_shipping_services_locator).click()
        self.waiter_with_assert('.image-intro')

    def go_to_dangerous_cargoes_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.dangerous_cargoes_services_locator).click()
        self.waiter_with_assert('.img-intro')

    def go_to_insurance_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.insurance_services_locator).click()
        self.waiter_with_assert('.intro-picture')

    def go_to_inspection_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.inspection_services_locator).click()
        self.waiter_with_assert('.services-box')

    def go_to_abandoned_cargoes_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.abandoned_cargoes_locator).click()
        self.waiter_with_assert('.section__hero__info')

    def go_to_certification_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.certification_service_locator).click()
        self.waiter_with_assert('.container-desk')

    def go_to_project_cargo_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.project_cargo_service_page_locator).click()
        self.waiter_with_assert('.intro-img')

    def go_to_customs_clearance_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.customs_clearance_locator).click()
        self.waiter_with_assert('.section__img-part')

    def go_to_custom_clearance_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.custom_clearance_service_locator).click()
        self.waiter_with_assert('.section__img-part')

    def go_to_survey_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.survey_cervices_locator).click()
        self.waiter_with_assert('.image-desc')

    def go_to_reefer_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.reefer_cargoes_cervices_locator).click()
        self.waiter_with_assert('.intro-img')

    def go_to_warehousing_services_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.warehousing_services_locator).click()
        self.waiter_with_assert('.images')

    def go_to_test_10_foot_containers_page(self):
        self.move_mouse_to_services()
        self.driver.find_element(*self.teen_foot_containers_locator).click()
        self.waiter_with_assert('.wrapper')