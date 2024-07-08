import os
# chromedriver_path = os.path.join(os.getcwd(), 'chromedriver', 'chromedriver')
current_dir = os.path.dirname(os.getcwd())
chromedriver_path = os.path.join(current_dir, 'chromedriver', 'chromedriver')


device_info = {
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

appium_port = 4723
