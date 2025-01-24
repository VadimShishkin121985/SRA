import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='class')
def chrome(request):
    # Настраиваем ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Новый режим headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")

    # Создаем сервис с явным указанием пути к ChromeDriver
    service = Service()
    
    # Инициализируем драйвер с сервисом и опциями
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)  # Добавляем неявное ожидание

    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def firefox(request):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.set_page_load_timeout(30)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()





#
#
#
# @pytest.fixture(scope='class')
# def chrome(request):
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_experimental_option('prefs',
#                                     {'credentials_enable_service': False, 'profile.password_manager_enabled': False})
#     options.add_argument('--disable-cache')
#     options.add_argument('--disable-extensions')
#     options.add_argument('--disable-infobars')
#     options.add_argument('--disable-browser-side-navigation')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--headless')
#     options.add_argument('--disable-web-security')
#     options.add_argument('--allow-running-insecure-content')
#     options.add_argument('--window-size=1920,1080')
#
#     try:
#         driver = webdriver.Chrome(options=options)
#         driver.maximize_window()
#         driver.set_page_load_timeout(120)
#         driver.implicitly_wait(60)
#
#         if request.cls:
#             request.cls.driver = driver
#
#         yield driver
#
#     finally:
#         if 'driver' in locals():
#             driver.quit()
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)
#
#     yield driver
#
#     # Делаем скриншот только если тест провалился
#     if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
#         driver.save_screenshot(f"screenshot_{request.node.name}.png")
#
#     driver.quit()
#
#
# # Хук для сохранения результата теста
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#    setattr(item, "rep_" + rep.when, rep)