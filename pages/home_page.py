from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class HomePage(BasePage):
    # Locators
    CAROUSEL = (By.ID, "//*[@id = 'spotlight_carousel']")
    SEARCH_FIELDS = (By.ID, "store_nav_search_term")
    BUTTON_SEARCH = (By.XPATH, "//*[@id= 'store_search_link']//img")

    def wait_page_load(self):
        return self.wait_visibility_for_element(self.CAROUSEL)

    def input_search_fields(self, name):
        return self.wait_visibility_for_element(self.SEARCH_FIELDS).send_keys(name)

    def click_button_search(self):
        return self.wait_visibility_for_element(self.BUTTON_SEARCH).click()

    # Methods
    def search(self, name):
        self.wait_page_load()
        self.input_search_fields(name)
        self.click_button_search()
