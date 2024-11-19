from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config_reader import ConfigReader


class WebDriverSingleton:
    _instance = None
    _driver = None

    file_config = "config/config.json"
    json_config = ConfigReader(file_config)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_driver()
        return cls._instance

    def _initialize_driver(self):
        if self._driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def get_driver(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance.driver

    @classmethod
    def quit_driver(cls):
        if cls._instance:
            cls._instance.driver.quit()
            cls._instance = None
