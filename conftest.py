import pytest


from config.data_reader import DataReader
from utilities.drivers import WebDriverSingleton

json_config = DataReader(DataReader.FILE_CONFIG)

@pytest.fixture(scope="function", autouse=False)
def driver():
    driver = WebDriverSingleton.get_driver()
    driver.get(json_config.get_data_key("URL"))
    yield driver
    WebDriverSingleton.quit_driver()
