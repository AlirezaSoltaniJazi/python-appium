import time

from assertpy import assert_that
from pytest import mark

from pages import DuckDuckGoPage


@mark.browse_page
def test_search_phrase_by_browser(android_driver_factory):
    with android_driver_factory() as driver:
        # Arrange
        browser = DuckDuckGoPage(driver)
        url = 'https://www.duckduckgo.com'

        # Act
        browser.open_address(url)
        browser.select_input_field()
        browser.enter_search_phrase('Alireza SoltaniJazi - Test Engineer')
        browser.close_keyboard()
        browser.click_search_button()
        result = browser.get_first_index_of_search_results()

        # Assert
        assert_that(result).is_equal_to('Alireza SoltaniJazi - Senior Software Test Engineer - BazaarPay | LinkedIn')
        time.sleep(5)
