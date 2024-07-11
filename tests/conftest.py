import os

import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def chrome(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs', {'credentials_enable_service': False, 'profile.password_manager_enabled': False})
    options.add_argument('--disable-cache')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    #service = Service(ChromeDriver().instal())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    if request.cls:
        request.cls.driver = driver
    yield driver
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This code executes after each test
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot if test failed
    if report.when == 'call' and report.failed:
        driver = item.funcargs['driver']
        screenshot_dir = 'screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_file = os.path.join(screenshot_dir, f"{item.name}.png")
        driver.save_screenshot(screenshot_file)
        # Attach screenshot to the report
        if report.longrepr:
            report.longrepr = f"{report.longrepr}\nScreenshot: {screenshot_file}"
