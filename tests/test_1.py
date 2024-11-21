import pytest

from config.config_constains import FILE_DATA_TEST, FILE_CONFIG
from config.config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_result_page import SearchPage

json_config = ConfigReader(FILE_CONFIG)
json_data = ConfigReader(FILE_DATA_TEST)
EXPECTED_TITLE = "Expected Page Title"


@pytest.mark.parametrize(
    'game_name, game_of_number',
    [
        pytest.param(*json_data.get_data("set1")),
        pytest.param(*json_data.get_data("set2")),
    ]
)
def test_list_game_with_price_desc1(driver, game_name, game_of_number):
    driver.get(json_config.get_url())
    hp = HomePage()
    assert hp.check_ready_state() == True
    hp.search(game_name)
    srp = SearchPage()
    unsorted_price, sorted_price = srp.sort_price_desc(game_of_number)
    assert unsorted_price != sorted_price, f"Actual result:{sorted_price}\nExpected result:{sorted_price}"
