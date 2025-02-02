import time
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120, poll_frequency=2,
            ignored_exceptions=[StaleElementReferenceException])

    def move_to_element(self, element):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(1)  # Небольшая пауза после наведения
        except Exception as e:
            print(f"Failed to move to element: {str(e)}")
            raise

    def wait_for_element_visibility(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            # Пробуем сначала найти элемент, потом проверить видимость
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.wait.until(lambda x: element.is_displayed())
            return element

    def privacy_setting(self):
        try:
            # Ждем появления shadow root
            shadow_host = self.wait.until(
                EC.presence_of_element_located((By.ID, 'usercentrics-root'))
            )
            
            # Пробуем несколько раз найти и кликнуть кнопку
            for _ in range(3):
                try:
                    deny_button = self.driver.execute_script(
                        'return arguments[0].shadowRoot.querySelector("[data-testid=\'uc-deny-all-button\']")',
                        shadow_host
                    )
                    if deny_button:
                        deny_button.click()
                        time.sleep(1)
                        return
                except Exception:
                    time.sleep(1)
                    continue
        except Exception as e:
            print(f"Failed to handle privacy settings: {str(e)}")
            # Продолжаем выполнение даже если не удалось закрыть окно
            pass

    def safe_click(self, element):
        """Безопасный клик по элементу с повторными попытками"""
        for _ in range(3):
            try:
                element.click()
                return True
            except Exception:
                time.sleep(1)
        return False