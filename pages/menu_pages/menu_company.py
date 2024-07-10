import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_page import BasePage


class MenuCompany(BasePage):
    _instance = None
    URL = 'https://www.searates.com/'

    def open(self) -> 'MenuCompany':
        self.driver.get(self.URL)
        return self

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.contact_us_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="Contact us"]')
        self.about_us_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="About us"]')
        self.faqs_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_icon"][normalize-space()="FAQs"]')
        self.blog_post_locator = (By.XPATH, '//div[@class="dropMenu"]//div[@class="dropMenu__list dropMenu__list_block dropMenu__list_footer dropMenu__list_max-width-full js-copy4"]//a[2]')
        self.blog_page_locator = (By.XPATH, '//div[@class="dropMenu__content js-drop-content"]//span[@class="dropMenu__text dropMenu__text_uppercase"][normalize-space()="blog"]')

    def move_mouse_to_company(self):
        menu_tools = self.driver.find_element(By.XPATH, '//a[@data-dropdown="company"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_tools).perform()
        time.sleep(2)

    def waiter_with_assert(self, selector):
        wait = WebDriverWait(self.driver, 50)
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element = wait.until(EC.visibility_of(element))
        assert element is not None, "Элемент не найден"

    def go_to_contact_us_page(self):
        self.move_mouse_to_company()
        self.driver.find_element(*self.contact_us_locator).click()
        self.waiter_with_assert('.IiUFLd')

    def go_to_about_us_page(self):
        self.move_mouse_to_company()
        self.driver.find_element(*self.about_us_locator).click()
        self.waiter_with_assert('.header__join-us')

    def go_to_faqs_page(self):
        self.move_mouse_to_company()
        self.driver.find_element(*self.faqs_locator).click()
        self.waiter_with_assert('._2LYQ4jKG4HZgg2IDcx1NcY')

    def go_to_blog_page(self):
        self.move_mouse_to_company()
        self.driver.find_element(*self.blog_page_locator).click()
        self.waiter_with_assert('.search')
        self.driver.back()

    def go_to_blog_post(self):
        self.move_mouse_to_company()
        self.driver.find_element(*self.blog_post_locator).click()
        self.waiter_with_assert('.search')
        self.driver.back()




