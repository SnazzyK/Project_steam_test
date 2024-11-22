from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class HomePage(BasePage):
    # Locators
    CAROUSEL = (By.ID, "spotlight_carousel")
    SEARCH_FIELDS = (By.ID, "store_nav_search_term")
    BUTTON_SEARCH = (By.XPATH, "//*[@id= 'store_search_link']//img")


    def search_fields(self, name):
        return self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELDS)).send_keys(name)

    def button_search(self):
         self.wait.until(EC.visibility_of_element_located(self.BUTTON_SEARCH)).click()

    # Methods
    def search(self, name):
        self.check_ready_state()
        self.search_fields(name)
        self.button_search()
