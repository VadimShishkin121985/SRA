import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import os
import time


@pytest.fixture
def chrome(request):
    """
    Фикстура с динамическим scope, который определяется маркером класса:
    @pytest.mark.browser_scope('class') - один браузер на весь класс
    @pytest.mark.browser_scope('function') - новый браузер для каждого теста
    """
    # Получаем scope из маркера или используем 'function' по умолчанию
    marker = request.node.get_closest_marker('browser_scope')
    scope = marker.args[0] if marker else 'function'

    # Создаем временную директорию для пользовательских данных Chrome
    temp_dir = os.path.join(tempfile.gettempdir(), f'chrome_test_{time.time()}')
    os.makedirs(temp_dir, exist_ok=True)

    # Настраиваем ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")

    # Отключаем Privacy Settings и другие уведомления
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_settings.popups': 0,
        'profile.default_content_setting_values.automatic_downloads': 1,
        'profile.managed_default_content_settings.javascript': 1,
        'profile.default_content_setting_values.cookies': 1,
        'profile.managed_default_content_settings.cookies': 1,
        'profile.default_content_setting_values.plugins': 1,
        'profile.default_content_setting_values.geolocation': 2,
        'profile.default_content_setting_values.media_stream': 2,
        'profile.default_content_setting_values.images': 1,
        'profile.default_content_setting_values.mixed_script': 1,
        'profile.default_content_setting_values.mouselock': 2,
        'profile.default_content_setting_values.protocol_handlers': 2,
        'profile.content_settings.exceptions.automatic_downloads.*.setting': 1
    })


    # Создаем сервис с явным указанием пути к ChromeDriver
    service = Service()

    #работа для ПК локально
    # service = webdriver.ChromeService(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver.set_page_load_timeout(30)  # Увеличиваем таймаут загрузки страницы
    # driver.implicitly_wait(20)  # Увеличиваем время ожидания элементов

    # Инициализируем драйвер работает для Github
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)  # Увеличиваем таймаут загрузки страницы
    driver.implicitly_wait(20)  # Увеличиваем время ожидания элементов

    # Устанавливаем драйвер для класса теста
    if request.cls:
        request.cls.driver = driver

    # Возвращаем драйвер
    yield driver
    driver.quit()

    if scope == 'function' or (scope == 'class' and request.node.cls._class_cleanup):
        try:
            driver.quit()
            # Очищаем временную директорию
            try:
                import shutil
                shutil.rmtree(temp_dir, ignore_errors=True)
            except:
                pass
        except Exception as e:
            print(f"Error closing browser: {str(e)}")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "browser_scope(scope): mark test class to set browser scope"
    )
