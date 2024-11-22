
from selenium.webdriver.common.by import By

from base_page.base_page import BasePage

from dataclasses import dataclass
from selenium.webdriver.support import expected_conditions as EC


@dataclass
class PriceInfo:
    price: str
    index: int


class SearchPage(BasePage):
    # Locators

    BUTTON_SORT = (By.ID, 'sort_by_dselect_container')
    PRICE_DESC = (By.ID, 'Price_DESC')
    ITEMS = (By.XPATH, "//a[@data-gpnav='item']")
    GRAY_BACKGROUND = (By.XPATH, "//*[contains(@style, 'opacity: 0.5')]")
    RESULT = (By.XPATH, "//*[@id='search_result_container' and not(contains(@style, 'opacity: 0.5'))]")
    PRICE = (By.XPATH, "//a[@data-gpnav='item']//div[contains(@class,'final_price')]")

    def click_button_sort(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_SORT)).click()

    def click_price_desc(self):
        self.wait.until(EC.visibility_of_element_located(self.PRICE_DESC)).click()

    def wait_background(self):
        self.wait_frequency.until(EC.presence_of_element_located(self.GRAY_BACKGROUND))
        self.wait.until(EC.presence_of_element_located(self.RESULT))

    def get_prices(self, value):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.PRICE))
        prices = [PriceInfo(price.text, idx) for idx, price in enumerate(elements[:value])]
        return prices

    def sort_price_desc(self):
        self.click_button_sort()
        self.click_price_desc()
        self.wait_background()
