from selenium.webdriver.support.wait import WebDriverWait

from utilities.drivers import WebDriverSingleton


class BasePage:
    TIMEOUT = 20

    def __init__(self):
        self.wait = WebDriverWait(WebDriverSingleton.get_driver(), self.TIMEOUT)
        self.wait_frequency = WebDriverWait(WebDriverSingleton.get_driver(), self.TIMEOUT, poll_frequency=0.1)




    def check_ready_state(self):
        page_load = self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        return page_load
