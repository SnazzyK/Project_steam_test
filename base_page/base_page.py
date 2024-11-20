from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def wait_visibility_for_element(self, locator, timeout=None):
        timeout = timeout or self.TIMEOUT
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_presents_for_element(self, locator, timeout=None):
        timeout = timeout or self.TIMEOUT
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def wait_visibility_of_all_for_element(self, locator, timeout=None):
        timeout = timeout or self.TIMEOUT
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_all_elements_located(locator)
        )
