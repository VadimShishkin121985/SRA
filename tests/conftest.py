
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
    # options.add_argument('--headless')
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


