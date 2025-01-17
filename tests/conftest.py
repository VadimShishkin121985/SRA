import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def chrome(request):
    # Устанавливаем нужную версию ChromeDriver
    chromedriver_autoinstaller.install()

    # Настройка опций для Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs',
                                    {'credentials_enable_service': False, 'profile.password_manager_enabled': False})
    options.add_argument('--disable-cache')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-browser-side-navigation')
    #options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--window-size=1920,1080')

    # Создание экземпляра ChromeDriver
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(330)

    # Привязка драйвера к классу, если он существует
    if request.cls:
        request.cls.driver = driver

    yield driver

    # Завершение работы драйвера после тестов
    driver.quit()