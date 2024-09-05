import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--user_name", action="store", default="abcde@gmail.com"       
    )
    parser.addoption(
        "--password", action="store", default="abcd@1234"       
    )
    parser.addoption(
        "--driver_path", action="store", default="/home/cbnits/Downloads/chromedriver"       
    )
    parser.addoption(
        "--search_product", action="store", default="iphone"
    )

@pytest.fixture(scope="class")
def invoke_driver(request):
    BASEURL = "https://www.amazon.in/"
    browser_name = request.config.getoption("browser_name")
    driver_path = request.config.getoption("driver_path")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        service_obj = Service(driver_path)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    # elif browser_name == "firefox":
    #     firefox_service = Service(driver_path)
    #     driver = webdriver.Firefox(service=firefox_service)


    driver.get(BASEURL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def passing_username_password(request):
    user_name = request.config.getoption("user_name")
    password = request.config.getoption("password")
    if user_name or password :
        request.cls.user_name = user_name
        request.cls.password = password
    yield

@pytest.fixture(scope="class")
def search_your_product(request):
    search_product = request.config.getoption("search_product")
    if search_product :
        request.cls.search_product = search_product
    yield





