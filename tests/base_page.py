import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
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

    def privacy_setting(self):
        time.sleep(5)  # Увеличиваем ожидание
        # Найти shadow host по ID
        wait = WebDriverWait(self.driver, 20)
        shadow_host = wait.until(
            EC.presence_of_element_located((By.ID, 'usercentrics-root'))
        )

        # Найти кнопку внутри Shadow DOM через JavaScript
        deny_button = self.driver.execute_script(
            'return arguments[0].shadowRoot.querySelector("[data-testid=\'uc-accept-all-button\']")',
            shadow_host
        )
        wait.until(EC.element_to_be_clickable(deny_button))
        deny_button.click()
        time.sleep(2)  # Ждем после клика