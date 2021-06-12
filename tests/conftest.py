from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.loaders import load_xlsx, write_data_dic_to_file
import settings as s
from selenium.webdriver.chrome.options import Options


# This section of coded is added to provide browser name from command line as parameter
# while executing the pytest tests
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="module")
def driver_setup(request):
    global driver
    print('-' * 10 + 'Driver - Setup' + '-' * 10)
    browser_name = request.config.getoption("browser_name")
    browser_name = browser_name.upper()
    if browser_name == "CHROME" and s.DOCKER == 'N':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "CHROME" and s.DOCKER == 'Y':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "FIREFOX":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "EDGE":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    yield driver
    print('-' * 10 + 'Driver - Tear Down' + '-' * 10)
    driver.close()
    driver.quit()


@pytest.fixture(scope="class")
def setup_demo():
    print("I will be executing first.")
    yield
    print("I will be executed last")


@pytest.fixture()
def data_load():
    print("User profile data being created.")
    return ["Vishva", "Thimmeogwda", "vishruth.cse@gmail.com"]


@pytest.fixture(params=[("Chrome", "Vishva", "Thimmegowda"), ("Firefox", "Vishva"), ("Edge", "JT")])
def crossbrowser(request):
    return request.param


# This section of the code runs after all the tests run
@pytest.fixture(scope='session', autouse=True)
def tests_setup():
    driver = None
    data = load_xlsx("./data/nopcommerce_test_data.xlsx")
    yield data
    print('-' * 10 + "Write output data sheet." + '-' * 10)
    write_data_dic_to_file(data)
    # To make sure all the opened web browser instances are closed properly
    if driver is not None:
        driver.quit()
