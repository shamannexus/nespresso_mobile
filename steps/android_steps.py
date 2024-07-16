import time

from appium.webdriver.common.appiumby import AppiumBy
from const import AndroidLocators as Locators
from const import UserData
from steps import NespressoAppSteps
from utils import launch_app, close_app


class AndroidNespressoAppSteps(NespressoAppSteps):

    def __init__(self, appium_driver):
        self.driver = appium_driver

    def handle_app_crash_on_launch(self, retries=3):
        """Handle app crash by closing and relaunching the app if a crash element is found."""
        for attempt in range(1, retries + 1):
            launch_app()
            time.sleep(5)  # TODO: Implement a waiter for app full load instead of sleep
            if self.driver.is_text_present('The service is not available', timeout=3):
                close_app()
            else:
                return True
        return False

    def handle_app_crash_on_log_in(self, retries=3):
        """Handle app crash by closing pop-up and pressing sign-in button until sign-out button appears."""
        for attempt in range(1, retries + 1):
            if self.driver.is_text_present('The service is not available', timeout=3):
                self.driver.click_button(Locators.close_alert_button_locator)
                self.driver.click_button(Locators.confirm_sign_in_btn)
            if self.driver.is_text_present('Sign out'):
                return True
        return False

    def handle_location_permission(self, action='permanently'):
        """Handle location permission dialog based on action provided."""
        action_button_locator = (AppiumBy.ID, getattr(Locators, f'permission_{action}_button'))
        if self.is_permission_popup_appear():
            if button := self.driver.find_element(action_button_locator):
                button.click()
                return True
        return False

    def is_permission_popup_appear(self) -> bool:
        """Check if location permission popup is present."""
        location_popup_element = (AppiumBy.ID, Locators.grant_dialog)
        return self.driver.find_element(location_popup_element)

    def handle_push_notification_popup(self):
        """Handle push notification popup by invoking an element click."""
        time.sleep(7)  # Wait to ensure elements are ready
        self.driver.click_button_when_ready(Locators.account_locator)
        if self.driver.find_element(Locators.pop_up_locator):
            if button := self.driver.find_element(Locators.decline_btn):
                button.click()

    def register_new_user(self, random_email):
        """Register a new user."""
        self.driver.click_button(Locators.account_locator)
        # TODO for some reason need this wait despite click_button_when_ready is using after,
        #  because sign_in_btn visible and clickable but actually works after few seconds of wait
        time.sleep(5)
        self.driver.click_button_when_ready(Locators.sign_in_btn)

        self.driver.click_button_when_ready(Locators.create_account_btn)

        self.driver.wait_for_element(Locators.web_view_locator)
        self.driver.switch_to_webview()

        self.driver.click_button(Locators.title_locator)

        self.driver.switch_to_native()
        option_locator = (AppiumBy.XPATH, f"//*[@text='{UserData.option_text}']")
        self.driver.click_button(option_locator)

        self.driver.switch_to_webview()
        self.driver.input_text(Locators.first_name_locator, UserData.first_name)
        self.driver.input_text(Locators.last_name_locator, UserData.last_name)

        self.driver.input_text(Locators.email_locator_when_register, random_email)
        self.driver.input_text(Locators.password_locator_when_register, UserData.password)
        self.driver.hide_keyboard()
        self.driver.switch_to_native()
        self.driver.click_button(Locators.continue_registration_btn_locator)

        # step 2
        self.driver.switch_to_webview()
        self.driver.input_text(Locators.address_line_1_locator, UserData.address_line_1)
        self.driver.input_text(Locators.town_locator, UserData.town)
        self.driver.input_text(Locators.postcode_locator, UserData.postcode)
        self.driver.input_text(Locators.phone_locator, UserData.phone_number)
        self.driver.hide_keyboard()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.switch_to_native()
        self.driver.click_button(Locators.continue_registration_btn_locator)

        # step 3
        self.driver.click_button(Locators.skip_btn_locator)
        self.driver.click_button(Locators.complete_registration_btn_locator)

        self.driver.wait_for_element(Locators.sign_out_btn)
        return bool(self.driver.find_element(Locators.sign_out_btn))

    def log_out(self):
        """Log out the current user."""
        self.driver.click_button_when_ready(Locators.sign_out_btn)
        self.driver.click_button(Locators.sign_out_confirm_btn)
        self.driver.wait_for_element(Locators.sign_in_btn)
        return bool(self.driver.find_element(Locators.sign_in_btn))

    def log_in(self, email):
        """Log in with the provided email."""
        self.driver.click_button(Locators.account_locator)
        # TODO for some reason need this wait despite click_button_when_ready is using after, because
        #  sign_in_btn visible and clickable but actually works after few seconds of wait
        time.sleep(3)
        self.driver.click_button_when_ready(Locators.sign_in_btn)
        self.driver.input_text(Locators.email_locator_when_log_in, email)
        self.driver.input_text(Locators.password_locator_when_log_in, UserData.password)

        self.driver.click_button_when_ready(Locators.confirm_sign_in_btn)

        assert self.handle_app_crash_on_log_in()

        self.driver.wait_for_element(Locators.sign_out_btn)
        return bool(self.driver.find_element(Locators.sign_out_btn))

    def order_product(self):
        """Order a product."""
        self.driver.click_button(Locators.shop_locator)
        self.driver.click_button(Locators.first_available_product_locator)
        self.driver.click_button(Locators.one_item_locator)
        self.driver.click_button(Locators.basket_locator)
        time.sleep(3)
        self.driver.click_button_when_ready(Locators.continue_btn_locator)
        time.sleep(3)
        self.driver.click_button_when_ready(Locators.boutique_radio_btn_locator)
        time.sleep(3)
        self.driver.click_button_when_ready(Locators.gps_btn_locator)
        time.sleep(3)
        self.driver.click_button_when_ready(Locators.first_shop_locator)
        self.driver.click_button_when_ready(Locators.continue_btn_locator)
        self.driver.click_button_when_ready(Locators.credit_card_radio_btn_locator)

        self.driver.input_text(Locators.credit_card_number_locator, UserData.credit_card_number)

        self.driver.input_text(Locators.ccv_code_locator, UserData.ccv_code)

        self.driver.click_button_when_ready(Locators.continue_btn_locator)

        element_exist = self.driver.is_text_present('Invalid Card number')
        if element_exist:
            return True
        return False
