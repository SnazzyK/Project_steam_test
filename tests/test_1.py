import pytest

from config.config_reader import ConfigReader
from conftest import driver
from pages.home_page import HomePage
from pages.search_result_page import SearchPage

file_config = "config/config.json"
json_config = ConfigReader(file_config)
file_data_test = "config/test_data.json"
json_data = ConfigReader(file_data_test)


@pytest.mark.parametrize(
    'creds',
    [
        pytest.param((json_data.get_game_data("set1", 'game1', "count1")), id='The Witcher, 10'),
        pytest.param((json_data.get_game_data("set2", 'game2', "count2")), id='Fallout, 20'),
    ]
)
def test_list_game_with_price_desc1(driver, creds):
    game_name, game_of_number = creds
    print("Start Test")
    driver.get(json_config.get_url())
    hp = HomePage(driver)
    hp.search(game_name)
    srp = SearchPage(driver)
    unsorted_prices, sorted_prices = srp.sort_price_desc(game_of_number)
    assert unsorted_prices != sorted_prices, "Price dont sorted!"
