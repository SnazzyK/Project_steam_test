from dataclasses import dataclass
from selenium.webdriver.support import expected_conditions as EC


@dataclass
class PriceInfo:
    price: str
    index: int


class PriceClass:
    def __init__(self, wait, PRICE):
        self.wait = wait
        self.PRICE = PRICE

    def get_prices(self, value):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.PRICE))

        prices = [PriceInfo(price.text, idx) for idx, price in enumerate(elements[:value])]

        return prices
