import pytest

from utilities.drivers import WebDriverSingleton


@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = WebDriverSingleton.get_driver()
    yield driver
    WebDriverSingleton.quit_driver()
