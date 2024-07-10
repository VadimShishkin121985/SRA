from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class MenuFooter:
    _instance = None
    URL = 'https://www.searates.com/'

    def open(self) -> 'MenuFooter':
        self.driver.get(self.URL)
        return self

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.footer_tools_le_locator = (By.XPATH, '//a[text()="Logistics Explorer"]')
        self.footer_tools_ct_locator = (By.XPATH, '//a[text()="Container Tracking"]')
        self.footer_tools_at_locator = (By.XPATH, '//a[text()="Air Tracking"]')
        self.footer_tools_ss_locator = (By.XPATH, '//a[text()="Ship Schedules"]')
        self.footer_tools_lc_locator = (By.XPATH, '//a[text()="Load Calculator"]')
        self.footer_tools_lm_locator = (By.XPATH, '//a[text()="Logistics Map"]')
        self.footer_tools_dt_locator = (By.XPATH, '//a[text()="Distance and Time"]')
        self.footer_tools_rt_locator = (By.XPATH, '//a[text()="Route Planner"]')
        self.footer_tools_sd_locator = (By.XPATH, '//a[text()="Smart Documents"]')
        self.footer_tools_dp_locator = (By.XPATH, '//a[text()="Developer Portal"]')
        self.footer_tools_request_it_locator = (By.XPATH, '//a[text()="Request an IT tool"]')
        self.footer_opportunities_for_shipper_locator = (By.XPATH, '//a[text()="For Shippers"]')
        self.footer_opportunities_for_carriers_locator = (By.XPATH, '//a[text()="For Carriers"]')
        self.footer_opportunities_for_integrations_locator = (By.XPATH, '//a[text()="Integrations"]')
        self.footer_opportunities_for_api_locator = (By.XPATH, '//a[text()="API"]')
        self.footer_opportunities_for_find_freight_routes_locator = (By.XPATH, '//a[text()="Find Freight Routes"]')
        self.footer_opportunities_for_shipping_line_directory_locator = (By.XPATH, '//a[text()="Shipping Lines Directory"]')
        self.footer_opportunities_for_maritime_locator = (By.XPATH, '//a[text()="Maritime"]')
        self.footer_company_blog_locator = (By.XPATH, '//a[text()="Blog"]')
        self.footer_company_careers_locator = (By.XPATH, '//a[text()="Careers"]')
        self.footer_company_copyright_locator = (By.XPATH, '//a[text()="Copyright"]')
        self.footer_company_help_locator = (By.XPATH, '//a[text()="Help"]')
        self.footer_contact_us_locator = (By.XPATH, '//a[text()="Contact us"]')
        self.footer_terms_locator = (By.XPATH, '//a[text()="Terms of service"]')
        self.footer_privacy_policy_locator = (By.XPATH, '//a[text()="Privacy Policy"]')
        self.footer_documents_templates_locator = (By.XPATH, '//a[text()="Documents templates"]')

    def move_mouse_to_footer(self):
        menu_tools = self.driver.find_element(By.XPATH, '//footer[@class="footer"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_tools).perform()
        time.sleep(3)

    def waiter_with_assert(self, selector):
        wait = WebDriverWait(self.driver, 50)
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        element = wait.until(element_present)
        assert element is not None, "Элемент не найден"

    def go_to_logistic_explorer_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_le_locator).click()
        self.waiter_with_assert('.le-header__hero')
        self.driver.back()
        pass

    def go_to_container_tracking_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_ct_locator).click()
        self.waiter_with_assert('#tracking_system_root')
        self.driver.back()

    def go_to_air_tracking_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_at_locator).click()
        self.waiter_with_assert('#tracking_system_root')
        self.driver.back()

    def go_to_ship_schedules_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_ss_locator).click()
        self.waiter_with_assert('#schedule')
        self.driver.back()

    def go_to_load_calculator_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_lc_locator).click()
        self.waiter_with_assert('.bFqpNG1R3Wtl2Vzq4oEY')
        self.driver.back()

    def go_to_logistic_map_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_lm_locator).click()
        self.waiter_with_assert('.main-content')
        self.driver.back()

    def go_to_distance_and_time_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_dt_locator).click()
        self.waiter_with_assert('.tCs9ghdPQNW7SMz-vn-Us')
        self.driver.back()

    def go_to_route_planer_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_rt_locator).click()
        self.waiter_with_assert('#map')
        self.driver.back()

    def go_to_smart_documents_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_sd_locator).click()
        self.waiter_with_assert('.wfetwx')
        self.driver.back()

    def go_to_developer_portal_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_dp_locator).click()
        self.waiter_with_assert('.text-center')
        self.driver.back()

    def go_to_request_it_tool_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_tools_request_it_locator).click()
        self.waiter_with_assert('.FLK0Cc')
        self.driver.back()

    def go_to_shippers_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_shipper_locator).click()
        self.waiter_with_assert('.header-left')
        self.driver.back()

    def go_to_carriers_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_carriers_locator).click()
        self.waiter_with_assert('.content')
        self.driver.back()

    def go_to_integrations_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_integrations_locator).click()
        self.waiter_with_assert('.type-programm')
        self.driver.back()

    def go_to_api_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_api_locator).click()
        self.waiter_with_assert('.products-list')
        self.driver.back()

    def go_to_find_freight_routes_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_find_freight_routes_locator).click()
        self.waiter_with_assert('.routes__title')
        self.driver.back()

    def go_to_shipping_lines_directory_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_shipping_line_directory_locator).click()
        self.waiter_with_assert('.shipping__list-main')
        self.driver.back()

    def go_to_maritime_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_opportunities_for_maritime_locator).click()
        self.waiter_with_assert('#map_canvas')
        self.driver.back()

    def go_to_blog_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_company_blog_locator).click()
        self.waiter_with_assert('.favorites__wrapper')
        self.driver.back()

    def go_to_careers_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_company_careers_locator).click()
        self.waiter_with_assert('.UVsHs1')
        self.driver.back()

    def go_to_copyright_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_company_copyright_locator).click()
        self.waiter_with_assert('.copy-header')
        self.driver.back()

    def go_to_help_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_company_help_locator).click()
        self.waiter_with_assert('._2XW0q_tjvjUGuWUfBlZYEw')
        self.driver.back()

    def go_to_contact_us_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_contact_us_locator).click()
        self.waiter_with_assert('.GJQ5in')
        self.driver.back()

    def go_to_terms_from_footer(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_terms_locator).click()
        self.waiter_with_assert('.panel-content')
        self.driver.back()

    def go_to_privacy_policy(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_privacy_policy_locator).click()
        self.waiter_with_assert('.main-content')
        self.driver.back()

    def go_to_documents_template(self):
        self.move_mouse_to_footer()
        self.driver.find_element(*self.footer_documents_templates_locator).click()
        self.waiter_with_assert('.document-download-btn')
        self.driver.back()


