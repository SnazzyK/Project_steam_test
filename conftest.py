import pytest


from config.config_reader import ConfigReader, FILE_CONFIG
from utilities.drivers import WebDriverSingleton

json_config = ConfigReader(FILE_CONFIG)

@pytest.fixture(scope="function", autouse=False)
def driver():
    driver = WebDriverSingleton.get_driver()
    driver.get(json_config.get_data("URL"))
    yield driver
    WebDriverSingleton.quit_driver()
