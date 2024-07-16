import os
current_dir = os.path.dirname(os.getcwd())
chromedriver_path = os.path.join(current_dir, 'chromedriver', 'chromedriver')


android_device_info = {
    'platformName': 'Android',
    'id': 'androidphone-1',
    'platform': 'AndroidPhone',
    'deviceName': 'Nespresso-testing',
    'platformVersion': '',
    'newCommandTimeout': 300,
    'androidInstallTimeout': 120000,
    'udid': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'appium:settings[waitForIdleTimeout]': 0,
    'chromedriver_autodownload': False,
    'chromedriverExecutable': chromedriver_path,
}

ios_device_info = {
    "platformName": "iOS",
    "deviceName": "iPhone Simulator",
    "platformVersion": "14.4",
    "app": "/path/to/ios/app",
    "automationName": "XCUITest",

}

appium_port = 4723
