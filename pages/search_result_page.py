from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_page.base_page import BasePage
from data_page.data_class import PriceInfo, PriceClass


class SearchPage(BasePage):
    # Locators

    BUTTON_SORT = (By.XPATH, "//*[@id='sort_by_dselect_container']")
    PRICE_DESC = (By.XPATH, "//*[@id='Price_DESC']")
    ITEMS = (By.XPATH, "//a[@data-gpnav='item']")
    GRAY_BACKGROUND = (By.XPATH, "//*[contains(@style, 'opacity: 0.5')]")
    RESULT = (By.XPATH, "//*[@id='search_result_container' and not(contains(@style, 'opacity: 0.5'))]")
    PRICE = (By.XPATH, "//a[@data-gpnav='item']//div[contains(@class,'final_price')]")

    def click_button_sort(self):
        return self.wait.until(EC.visibility_of_element_located(self.BUTTON_SORT)).click()

    def click_price_desc(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRICE_DESC)).click()

    def wait_background(self):
        def wait_grey_back():
            return self.wait.until(EC.presence_of_element_located(self.GRAY_BACKGROUND))

        def wait_not_grey_back():
            return self.wait.until(EC.presence_of_element_located(self.RESULT))

        wait_grey_back()
        wait_not_grey_back()

    def get_prices(self, value):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.PRICE))
        prices = [PriceInfo(price.text, idx) for idx, price in enumerate(elements[:value])]
        return prices

    def sort_price_desc(self, value):
        unsorted_price = self.get_prices(value)
        self.click_button_sort()
        self.click_price_desc()
        self.wait_background()
        sorted_price = self.get_prices(value)
        return unsorted_price, sorted_price
