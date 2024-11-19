from selenium.webdriver.common.by import By

from base_page.base_class import BasePage


class HomePage(BasePage):
    # Locators
    SEARCH_FIELDS = (By.XPATH, "//input[@id = 'store_nav_search_term']")
    BUTTON_SEARCH = (By.XPATH, "//*[@id = 'store_search_link']//img")

    def input_search_fields(self, name):
        return self.wait_visibility_for_element(self.SEARCH_FIELDS).send_keys(name)

    def click_button_search(self):
        return self.wait_visibility_for_element(self.BUTTON_SEARCH).click()

    # Methods
    def search(self, name):
        self.input_search_fields(name)
        self.click_button_search()
