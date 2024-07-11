import os

import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Фикстура для инициализации одного экземпляра браузера на всю сессию
@pytest.fixture(scope='class')
def chrome(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs',
                                    {'credentials_enable_service': False, 'profile.password_manager_enabled': False})
    options.add_argument('--disable-cache')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--window-size=1920,1080')

    # Используем WebDriver Manager для автоматической установки и обновления ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.set_page_load_timeout(120)
    driver.implicitly_wait(60)

    if request.cls:
        request.cls.driver = driver

    yield driver

    driver.quit()


# Фикстура для инициализации нового экземпляра браузера для каждого теста
@pytest.fixture(scope="function")
def browser(request):
    options = webdriver.ChromeOptions()
    # Добавьте любые необходимые опции браузера

    driver = webdriver.Chrome(options=options)

    yield driver

    # Захватываем скриншот при возникновении ошибки
    if request.node.rep_call.failed:
        driver.save_screenshot(f"screenshot_{request.node.name}.png")

    driver.quit()


@pytest.fixture(scope="function")
def browser():
    # Инициализируем браузер
    options = webdriver.ChromeOptions()
    # Добавьте любые необходимые опции браузера
    driver = webdriver.Chrome(options=options)

    # Предоставляем браузер тесту
    yield driver

    # Закрываем браузер после каждого теста
    driver.quit()

