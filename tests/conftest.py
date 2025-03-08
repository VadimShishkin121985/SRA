import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import os
import time
import shutil

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def chrome(request):
    """
    Фикстура с динамическим scope, который определяется маркером класса:
    @pytest.mark.browser_scope('class') - один браузер на весь класс
    @pytest.mark.browser_scope('function') - новый браузер для каждого теста
    """
    # Определяем scope (по умолчанию function)
    marker = request.node.get_closest_marker('browser_scope')
    scope = marker.args[0] if marker and marker.args else 'function'

    # Создаем временную директорию для пользовательских данных Chrome
    temp_dir = os.path.join(tempfile.gettempdir(), f'chrome_test_{int(time.time())}')

    # Настраиваем ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False
    })

    # Инициализируем WebDriver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(20)

    if request.cls:
        request.cls.driver = driver

    yield driver  # Передача драйвера в тест

    driver.quit()  # Закрываем браузер после теста
    shutil.rmtree(temp_dir, ignore_errors=True)  # Удаляем временные файлы

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # Получаем результат выполнения теста
#     outcome = yield
#     rep = outcome.get_result()
#
#     # Если тест зафейлился, добавляем задержку
#     if rep.when == "call" and rep.failed:
#         print(f"Test {item.name} failed. Waiting for 800 seconds before proceeding...")
#         time.sleep(800)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "browser_scope(scope): mark test class to set browser scope"
    )
