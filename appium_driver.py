from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from config import device_info, appium_port
from config import appium_port

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver import Remote

class AppiumDriver:

    def __init__(self, device_info, command_executor=f"http://localhost:{appium_port}/wd/hub"):
        if device_info['platformName'].lower() == 'android':
            options = UiAutomator2Options().load_capabilities(device_info)
        elif device_info['platformName'].lower() == 'ios':
            options = XCUITestOptions().load_capabilities(device_info)
        else:
            raise ValueError("Unsupported platform specified")
        self.driver = Remote(command_executor=command_executor, options=options)

# class AppiumDriver:
#
#     def __init__(self, command_executor=f"http://localhost:{appium_port}/wd/hub"):
#         options = UiAutomator2Options().load_capabilities(device_info)
#         self.driver = Remote(command_executor=command_executor, options=options)

    def find_element(self, locator):
        """
        Find a single element in the current context.

        :param locator: Tuple with (AppiumBy.ID, 'element_id') or other locators.
        :return: WebElement if found, else None.
        """
        try:
            return self.driver.find_element(*locator)
        except (NoSuchElementException, WebDriverException):
            return None

    def switch_to_webview(self):
        """
        Switch the context to the first available WEBVIEW context.

        :return: True if successfully switched, otherwise raises an Exception.
        """
        webview_context = None
        for context in self.driver.contexts:
            if 'WEBVIEW' in context:
                webview_context = context
                break

        if webview_context:
            self.driver.switch_to.context(webview_context)

            if 'WEBVIEW' in self.driver.current_context:
                return True
        else:
            raise Exception("No WebView context found")

    def switch_to_native(self):
        """
        Switch the context back to the NATIVE_APP context.
        """
        self.driver.switch_to.context(self.driver.contexts[0])

    def hide_keyboard(self):
        """
        Hide the on-screen keyboard if it is visible.
        """
        self.driver.hide_keyboard()

    def execute_script(self, script):
        """
        Execute JavaScript in the current context.

        :param script: The JavaScript code to execute.
        """
        self.driver.execute_script(script)

    def quit(self):
        """
        Quit the WebDriver session.
        """
        self.driver.quit()

    def wait_for_element(self, locator, timeout=15):
        """
        Wait for an element to be present in the DOM and be visible.

        :param locator: Tuple with (AppiumBy.ID, 'element_id') or other locators
        :param timeout: Maximum time to wait for the element. Default is 15 seconds.
        """
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=15):
        """
        Wait for an element to be present in the DOM and be clickable.

        :param locator: Tuple with (AppiumBy.ID, 'element_id') or other locators
        :param timeout: Maximum time to wait for the element. Default is 15 seconds.
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_button(self, locator):
        """
        Click a button identified by the locator.

        :param locator: Tuple with (AppiumBy.ID, 'element_id') or other locators.
        """
        self.wait_for_element(locator)
        button = self.find_element(locator)
        button.click()

    def click_button_when_ready(self, locator):
        """
        Click a button when it becomes clickable.

        :param locator: Tuple with (AppiumBy.ID, 'element_id') or other locators.
        """
        self.wait_for_element_to_be_clickable(locator)
        button = self.find_element(locator)
        button.click()

    def input_text(self, locator, key):
        """
        Enter text into a text input field identified by the locator.

        :param locator: Tuple with (AppiumBy.ID, 'element_id') or other locators.
        :param key: The text to enter into the input field.
        """
        self.wait_for_element(locator)
        button = self.find_element(locator)
        button.send_keys(key)

    def is_text_present(self, text, timeout=15):
        """
        Check if the specified text is present in the current context.

        :param text: The text to search for.
        :param timeout: Maximum time to wait for the text to be present. Default is 15 seconds.
        :return: True if the text is found within the timeout, otherwise False.
        """
        try:
            locator = (AppiumBy.XPATH, f"//*[contains(@text, '{text}')]")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
