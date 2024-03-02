from typing import Final


class AppConfig:
    FIREFOX_CONFIG: Final[dict] = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "appium:platformVersion": "9.0",
        'appPackage': 'org.mozilla.firefox',
        'appActivity': 'org.mozilla.fenix.HomeActivity',
        # 'device_name': 'emulator-5556',
        "appium:grantPermissions": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "resetKeyboard": True
    }
    CHROME_CONFIG: Final[dict] = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "appium:platformVersion": "10.0",
        'appPackage': 'com.android.chrome',
        'appActivity': 'org.chromium.android_webview.devui.MainActivity',
        # 'device_name': 'emulator-5556',
        "appium:grantPermissions": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "resetKeyboard": True
    }


class AppServer:
    APPIUM_PORT = 4727
    APPIUM_HOST = '127.0.0.1'
