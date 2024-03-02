from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DuckDuckGoPage:
    _SEARCH_INPUT_FIELD = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                     '/android.widget.FrameLayout/android.widget.LinearLayout'
                                     '/android.widget.FrameLayout/android.widget.LinearLayout'
                                     '/android.widget.FrameLayout/android.widget.FrameLayout'
                                     '/android.widget.FrameLayout/android.view.ViewGroup'
                                     '/android.view.ViewGroup/android.view.ViewGroup[1]'
                                     '/android.widget.FrameLayout/android.webkit.WebView'
                                     '/android.view.View/android.view.View/android.view.'
                                     'View[2]/android.widget.EditText')
    _SEARCH_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                '/android.widget.FrameLayout/android.widget.LinearLayout/'
                                'android.widget.FrameLayout/android.widget.LinearLayout/'
                                'android.widget.FrameLayout/android.widget.FrameLayout/'
                                'android.widget.FrameLayout/android.view.ViewGroup/'
                                'android.view.ViewGroup/android.view.ViewGroup[1]/'
                                'android.widget.FrameLayout/android.webkit.WebView/'
                                'android.view.View/android.view.View/'
                                'android.view.View[2]/android.widget.Button[2]')

    def __init__(self, driver: WebDriver, explicit_time: int = 20):
        self._driver = driver
        self._explicit_wait = WebDriverWait(driver, explicit_time)

    def open_address(self, address: str):
        self._driver.get(address)

    def select_input_field(self):
        condition = expected_conditions.element_to_be_clickable(self._SEARCH_INPUT_FIELD)
        search_input: WebElement = self._explicit_wait.until(condition)
        search_input.click()

    def enter_search_phrase(self, phrase: str):
        condition = expected_conditions.visibility_of_element_located(self._SEARCH_INPUT_FIELD)
        search_input: WebElement = self._explicit_wait.until(condition)
        search_input.send_keys(phrase)

    def close_keyboard(self):
        self._driver.hide_keyboard()

    def click_search_button(self):
        condition = expected_conditions.visibility_of_element_located(self._SEARCH_BUTTON)
        search_input: WebElement = self._explicit_wait.until(condition)
        search_input.click()
