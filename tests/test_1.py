import pytest

from config.config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_result_page import SearchPage

json_config = ConfigReader(ConfigReader.FILE_CONFIG)
json_data = ConfigReader(ConfigReader.FILE_DATA_TEST)


@pytest.mark.parametrize(
    'game_name,game_of_number',
    [
        pytest.param(*json_data.get_data("set1", 'game1', "count1"), id='The Witcher, 10'),
        pytest.param(*json_data.get_data("set2", 'game2', "count2"), id='Fallout, 20'),
    ]
)
def test_list_game_with_price_desc1(driver, game_name, game_of_number):
    driver.get(json_config.get_url())
    hp = HomePage(driver)
    hp.search(game_name)
    srp = SearchPage(driver)
    unsorted_prices, sorted_prices = srp.sort_price_desc(game_of_number)
    assert unsorted_prices != sorted_prices, f"Actual result:Price dont sorted\nExpected result:Price sorted!"
