from selenium.webdriver.support.wait import WebDriverWait

from utilities.drivers import WebDriverSingleton



class BasePage:
    TIMEOUT = 20

    def __init__(self):
        self.wait = WebDriverWait(WebDriverSingleton.get_driver(), self.TIMEOUT)

