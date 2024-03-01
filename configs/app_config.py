from typing import Final


class AppConfig:
    FIREFOX_CONFIG: Final[dict] = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        'appPackage': 'org.mozilla.firefox',
        'appActivity': 'org.mozilla.fenix.HomeActivity',
        'device_name': 'emulator-5556'
    }
    CHROME_CONFIG: Final[dict] = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        'appPackage': 'com.android.chrome',
        'appActivity': 'org.chromium.android_webview.devui.MainActivity',
        'device_name': 'emulator-5556'
    }



class AppServer:
    APPIUM_PORT = 4727
    APPIUM_HOST = '127.0.0.1'
