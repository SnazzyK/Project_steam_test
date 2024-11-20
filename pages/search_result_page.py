from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class SearchPage(BasePage):
    # Locators

    BUTTON_SORT = (By.ID, 'sort_by_dselect_container')
    PRICE_DESC = (By.ID, 'Price_DESC')
    ITEMS = (By.XPATH, "//a[@data-gpnav='item']")
    PRICE = (By.XPATH, "//a[@data-gpnav='item']//div[contains(@class,'final_price')]")
    GRAY_BACKGROUND = (By.XPATH, "//*[contains(@style, 'opacity: 0.5')]")
    RESULT = (By.XPATH, "//*[@id='search_result_container' and not(contains(@style, 'opacity: 0.5'))]")

    def click_button_sort(self):
        return self.wait_visibility_for_element(self.BUTTON_SORT).click()

    def click_price_desc(self):
        return self.wait_visibility_for_element(self.PRICE_DESC).click()

    def wait_load(self):
        def wait_grey_back():
            return self.wait_presents_for_element(self.GRAY_BACKGROUND)

        def wait_not_grey_back():
            return self.wait_presents_for_element(self.RESULT)

    def get_prices(self, value):
        price_elements = self.wait_visibility_of_all_for_element(self.PRICE)
        return [price.text for price in price_elements[:value]]

    def sort_price_desc(self, value):
        unsorted_prices = self.get_prices(value)
        self.click_button_sort()
        self.click_price_desc()
        self.wait_load()
        sorted_price = self.get_prices(value)
        return unsorted_prices, sorted_price
