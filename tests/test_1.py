import pytest

from config.config_reader import ConfigReader, FILE_CONFIG
from pages.home_page import HomePage
from pages.search_result_page import SearchPage

FILE_DATA_TEST = "config/test_data.json"
json_config = ConfigReader(FILE_CONFIG)
json_data = ConfigReader(FILE_DATA_TEST)


@pytest.mark.parametrize(
    'game_name, game_of_number',
    [
        pytest.param(*json_data.get_data("set1")),
        pytest.param(*json_data.get_data("set2")),
    ]
)
def test_list_game_with_price_desc1(driver, game_name, game_of_number):
    hp = HomePage()
    assert hp.check_ready_state()
    hp.search(game_name)
    srp = SearchPage()
    unsorted_price = srp.get_prices(game_of_number)
    srp.sort_price_desc()
    sorted_price = srp.get_prices(game_of_number)
    assert unsorted_price != sorted_price, f"Actual result:{sorted_price}\nExpected result:{sorted_price}"
