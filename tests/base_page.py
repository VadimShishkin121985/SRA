from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def wait_for_element_visibility(self, locator):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
