from selenium import webdriver
from Utilities.customLogger import GetLogger
from selenium.webdriver.chrome.options import Options
import pytest
from Utilities.readProperties import Config

@pytest.fixture()
def setup(browser, config_section):
    print(config_section)
    config = Config.read_config(config_section)
    if browser == "chrome":
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='C:/Users/user/Downloads/chromedriver.exe', options=options)
    elif browser == "firefox":
        driver = webdriver.Chrome(executable_path='C:/Users/user/Downloads/geckodriver.exe')
    else:
        # Default uses Chrome
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='C:/Users/user/Downloads/chromedriver.exe', options=options)
    logger = GetLogger.get_Logger(file=".//Logs/test_login.log")
    logger.info("Opening URL...")
    driver.get(config["url"])
    yield driver, logger, config
    logger.info("Closing Window...")
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--config_section")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def config_section(request):
    return request.config.getoption("--config_section")

def pytest_configure(config):
    config._metadata['Project Name']= 'Amazon Automation'
    config._metadata['ModuleName']= 'Login'
    config._metadata['Tester']='Shilpa'

    @pytest.mark.optionalhook
    def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)















    

