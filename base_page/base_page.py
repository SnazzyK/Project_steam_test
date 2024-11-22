from selenium.webdriver.support.wait import WebDriverWait

from config.data_reader import DataReader
from utilities.drivers import WebDriverSingleton

json_config = DataReader(DataReader.FILE_CONFIG)


class BasePage:
    POOL_FREQUENCY = float(json_config.get_data_key("poll_frequency"))

    def __init__(self):
        self.wait = WebDriverWait(WebDriverSingleton.get_driver(), json_config.get_data_key("TIMEOUT"))
        self.wait_frequency = WebDriverWait(WebDriverSingleton.get_driver(), json_config.get_data_key("TIMEOUT"),
                                            self.POOL_FREQUENCY)

    def wait_ready_state(self):
        page_load = self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
