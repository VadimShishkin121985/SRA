from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.base_page import BasePage


class RequestAQuote(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        number_quote = None
        self.driver: WebDriver = driver
        self.enter_hs_code_locator = (By.XPATH, '//input[@type="text"]')
        self.choose_freight_all_kind_locator = (By.XPATH, '//div[@class="pj_tV1"]')
        self.next_button_locator = (By.XPATH, '//div[@class="WTsBDL uQ_dEi hC2VyB"]')
        self.transportation_by_locator = (By.XPATH, '//div[@class="Htwz17"]')
        self.transportation_type_auto_locator = (By.XPATH, '//li[@class="GNa0e1"]/span[text()="All transport"]')
        self.input_weight_locator = (By.XPATH, '//input[@id="weight"]')
        self.input_volume_locator = (By.XPATH, '//input[@id="volume"]')
        self.location_from_locator = (By.XPATH, '//input[@id="autocomplete_from"]')
        self.text1_from_locator = (By.XPATH, '//p[text()="Ukraine, Odessa Oblast"]')
        self.text2_from_locator = (By.XPATH, '//span[text()="Odesa"]')
        self.location_to_locator = (By.XPATH, '//input[@id="autocomplete_to"]')
        self.text1_to_locator = (By.XPATH, '//span[text()="Shanghai"]')
        self.redy_to_load_locator = (By.XPATH, '//div[@class="KLr4PD"]')
        self.current_date_locator = (By.XPATH, '(//div[@data-is-default-selectable="true"])[2]')
        self.additional_information_locator = (By.XPATH, '//textarea')
        self.track_request_status_locator = (By.XPATH, '//div[@class="WTsBDL uQ_dEi ec1hiy"]')
        self.request_number_locator = (By.XPATH, '//h2[@class="_SR9Fx"]')



    def fill_hs_code_field(self):
        self.driver.find_element(*self.enter_hs_code_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.choose_freight_all_kind_locator).click()
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="iSymS3"]')))
        assert element is not None, "Element not found on page"
        pass

    def click_next_button(self):
        self.driver.find_element(*self.next_button_locator).click()
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1')))
        assert element is not None, "Element not found on page"
        pass

    def choose_transportation_auto(self):
        self.driver.find_element(*self.transportation_by_locator).click()
        self.driver.find_element(*self.transportation_type_auto_locator).click()
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="All transport"]')))
        assert element is not None, "Element not found on page"
        pass

    def fill_input_weight(self):
        weight = 50
        self.driver.find_element(*self.input_weight_locator).send_keys(weight)
        pass

    def fill_input_volume(self):
        volume = 50
        self.driver.find_element(*self.input_volume_locator).send_keys(volume)
        pass

    def fill_location_from(self):
        city_from = 'Odessa'
        self.driver.find_element(*self.location_from_locator).send_keys(city_from)
        time.sleep(2)
        self.driver.find_element(*self.text1_from_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.text2_from_locator).click()
        pass

    def fill_location_to(self):
        city_to = 'Shanghai'
        self.driver.find_element(*self.location_to_locator).send_keys(city_to)
        time.sleep(2)
        self.driver.find_element(*self.text1_to_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.text1_to_locator).click()
        pass

    def choose_date_redy_to_load(self):
        self.driver.find_element(*self.redy_to_load_locator).click()
        self.driver.find_element(*self.current_date_locator).click()
        self.driver.find_element(*self.current_date_locator).click()
        pass

    def fill_additional_information(self):
        info = 'This is a test request, please do not process this request.'
        self.driver.find_element(*self.additional_information_locator).send_keys(info)
        pass

    def get_quote_number(self):
        number_quote = self.driver.find_element(*self.request_number_locator)
        return number_quote.text[:-6]

    def confirmation_of_creation_request(self):
        self.driver.find_element(*self.track_request_status_locator).click()


        pass








    def chose_transportation_by_for_fcl(self):
        self.driver.find_element(*self.choose_transportation_by_locator).click()
        transportation_by_select1 = self.driver.find_element(By.ID, 'react-select-3-option-0-0')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_by_select1).click().perform()
        pass

    def chose_transportation_by_for_lcl(self):
        self.driver.find_element(*self.choose_transportation_by_locator).click()
        transportation_by_select = self.driver.find_element(By.ID, 'react-select-3-option-0-1')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_by_select).click().perform()
        pass

    def chose_transportation_by_for_bulk(self):
        self.driver.find_element(*self.choose_transportation_by_locator).click()
        transportation_by_select = self.driver.find_element(By.ID, 'react-select-3-option-0-2')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_by_select).click().perform()
        pass

    def choose_container_type_and_quantity(self):
        quantity = 4
        self.driver.find_element(*self.choose_type_container_locator).click()
        type_container_select = self.driver.find_element(By.ID, 'react-select-4-option-0')
        actions = ActionChains(self.driver)
        actions.move_to_element(type_container_select).click().perform()
        self.driver.find_element(*self.input_quantity_of_containers_locator).send_keys(quantity)
        pass

    def choose_container_type_and_quantity_for_land(self):
        quantity = 4
        self.driver.find_element(*self.choose_type_container_locator).click()
        time.sleep(2)
        type_container_select = self.driver.find_element(By.ID, 'react-select-7-option-2')
        actions = ActionChains(self.driver)
        actions.move_to_element(type_container_select).click().perform()
        self.driver.find_element(*self.input_quantity_of_containers_locator).send_keys(quantity)
        pass

    def choose_container_type_and_quantity_for_land_ftl(self):
        quantity = 4
        self.driver.find_element(*self.choose_truck_type_locator).click()
        time.sleep(2)
        type_container_select = self.driver.find_element(By.ID, 'react-select-7-option-2')
        actions = ActionChains(self.driver)
        actions.move_to_element(type_container_select).click().perform()
        self.driver.find_element(*self.input_quantity_of_containers_locator).send_keys(quantity)
        pass

    def choose_ship_type_for_bulk(self):
        element_to_scroll = self.driver.find_element(*self.ship_type_for_bulk_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_to_scroll)
        time.sleep(2)
        self.driver.find_element(*self.ship_type_for_bulk_locator).click()
        ship_type = self.driver.find_element(By.ID, 'react-select-6-option-2')
        actions = ActionChains(self.driver)
        actions.move_to_element(ship_type).click().perform()

        pass

    def fill_weight_field(self):
        weight_in_mt = 10
        self.driver.find_element(*self.input_weight_locator).send_keys(weight_in_mt)
        pass

    def fill_volume_field(self):
        volume_m3 = 8
        self.driver.find_element(*self.input_volume_locator).send_keys(volume_m3)
        pass

    def fill_point_from(self):
        port_from = 'Odesa'
        time.sleep(2)
        element_to_scroll = self.driver.find_element(*self.input_from_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_to_scroll)
        time.sleep(2)
        test123 = self.wait_for_element_visibility(self.input_from_locator)
        test123.send_keys(port_from)
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_city_from_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_port_from_locator).click()
        pass

    def fill_point_from_for_bulk(self):
        port_from = 'Odesa'
        time.sleep(2)
        element_to_scroll = self.driver.find_element(*self.input_from_for_bulk_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_to_scroll)
        time.sleep(2)
        test123 = self.wait_for_element_visibility(self.input_from_for_bulk_locator)
        test123.send_keys(port_from)
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_city_from_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_port_from_locator).click()
        pass

    def fill_point_to(self):
        port_to = 'Singapore'
        self.driver.find_element(*self.input_to_locator).send_keys(port_to)
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_city_to_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_port_to_locator).click()
        pass

    def fill_point_to_for_bulk(self):
        port_to = 'Singapore'
        self.driver.find_element(*self.input_to_for_bulk_locator).send_keys(port_to)
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_city_to_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.autocomplete_port_to_locator).click()
        pass

    def fill_redy_to_load(self):
        self.driver.find_element(*self.ready_to_load_locator).click()
        self.driver.find_element(*self.current_day_locator).click()
        pass

    def fill_additional_info(self):
        text_description = 'This is a test request, please do not process this request.'
        self.driver.find_element(*self.additional_information_locator).send_keys(text_description)
        pass

    def fill_firs_name(self):
        first_name = 'Something'
        self.driver.find_element(*self.first_name_locator).send_keys(first_name)
        pass

    def fill_last_name(self):
        last_name = 'New'
        self.driver.find_element(*self.last_name_locator).send_keys(last_name)
        pass

    def fill_e_mail(self):
        e_mail = '121985ops@gmail.com'
        e_mail_input = self.driver.find_element(By.XPATH, '//input[@name="user.email"]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", e_mail_input)
        time.sleep(2)
        e_mail_input.send_keys(e_mail)
        pass

    def fill_company(self):
        company_name = 'Test'
        self.driver.find_element(*self.company_locator).send_keys(company_name)
        pass

    def button_send(self):
        self.driver.find_element(*self.button_send_locator).click()
        pass

    def contact_phone_number(self):
        number_phone = 677821582
        self.driver.find_element(*self.phone_code_locator).click()
        # country_code_select = self.driver.find_element(By.ID, 'react-select-5-option-231')
        # actions = ActionChains(self.driver)
        # actions.scroll_to_element(country_code_select).click().perform()
        country_code_select = self.driver.find_element(By.ID, 'react-select-5-option-231')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", country_code_select)
        time.sleep(2)
        country_code_select.click()
        self.driver.find_element(*self.phone_number_locator).send_keys(number_phone)
        pass

    def loading_discharging_rate_for_bulk(self):
        mt_day = 800
        self.driver.find_element(*self.loading_rate_locator).send_keys(mt_day)
        self.driver.find_element(*self.discharging_rate).send_keys(mt_day)
        pass

    def fill_cross_weight(self):
        cross_weight = 50000
        self.driver.find_element(*self.cross_weight_locator).send_keys(cross_weight)
        pass

    def choose_delivery_type_land(self):
        self.driver.find_element(*self.delivery_type_land_locator).click()
        pass

    def choose_delivery_type_air(self):
        self.driver.find_element(*self.delivery_type_air_locator).click()
        pass

    def choose_delivery_type_auto(self):
        self.driver.find_element(*self.delivery_type_auto_locator).click()
        pass

    def choose_transportation_by_land_fcl(self):
        self.driver.find_element(*self.choose_transportation_by_land_locator).click()
        transportation_type_fcl = self.driver.find_element(By.ID, 'react-select-6-option-0-0')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_type_fcl).click().perform()
        pass

    def choose_transportation_by_land_ftl(self):
        self.driver.find_element(*self.choose_transportation_by_land_locator).click()
        transportation_type_ftl = self.driver.find_element(By.ID, 'react-select-6-option-0-1')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_type_ftl).click().perform()
        pass

    def choose_transportation_by_land_ltl(self):
        self.driver.find_element(*self.choose_transportation_by_land_locator).click()
        transportation_type_ltl = self.driver.find_element(By.ID, 'react-select-6-option-0-2')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_type_ltl).click().perform()
        pass

    def choose_transportation_by_land_fwl(self):
        self.driver.find_element(*self.choose_transportation_by_land_locator).click()
        transportation_type_ltl = self.driver.find_element(By.ID, 'react-select-6-option-1-1')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_type_ltl).click().perform()
        pass

    def choose_transportation_by_air_standard_cargo(self):
        self.driver.find_element(*self.choose_transportation_by_air_locator).click()
        transportation_type_ltl = self.driver.find_element(By.ID, 'react-select-6-option-0-0')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_type_ltl).click().perform()
        pass

    def choose_transportation_by_air_uld_container(self):
        self.driver.find_element(*self.choose_transportation_by_air_locator).click()
        transportation_type_ltl = self.driver.find_element(By.ID, 'react-select-6-option-0-1')
        actions = ActionChains(self.driver)
        actions.move_to_element(transportation_type_ltl).click().perform()
        pass

