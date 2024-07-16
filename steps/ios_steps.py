import time

from const import IosLocators as Locators
from const import UserData
from steps import NespressoAppSteps


class IosNespressoAppSteps(NespressoAppSteps):

    def __init__(self, appium_driver):
        self.driver = appium_driver

    def handle_app_crash_on_launch(self, retries=3):
        raise NotImplementedError

    def handle_app_crash_on_log_in(self, retries=3):
        raise NotImplementedError

    def handle_location_permission(self, action='permanently'):
        raise NotImplementedError

    def is_permission_popup_appear(self) -> bool:
        raise NotImplementedError

    def handle_push_notification_popup(self):
        raise NotImplementedError

    def register_new_user(self, random_email):
        raise NotImplementedError

    def log_out(self):
        raise NotImplementedError

    def log_in(self, email):
        self.driver.click_button(Locators.account_locator)
        time.sleep(3)
        self.driver.click_button_when_ready(Locators.sign_in_btn)
        self.driver.input_text(Locators.email_locator_when_log_in, email)
        self.driver.input_text(Locators.password_locator_when_log_in, UserData.password)

        self.driver.click_button_when_ready(Locators.confirm_sign_in_btn)

        assert self.handle_app_crash_on_log_in()

        self.log_in_using_biometric()

        self.driver.wait_for_element(Locators.sign_out_btn)
        return bool(self.driver.find_element(Locators.sign_out_btn))

    def order_product(self):
        raise NotImplementedError

    def log_in_using_biometric(self):
        # Implementation for logging in using biometric authentication
        if self.driver.is_text_present('Use your fingerprint'):
            self.driver.click_button(Locators.biometric_confirm_button_locator)
        elif self.driver.is_text_present('Use Face ID'):
            self.driver.click_button(Locators.face_id_confirm_button_locator)
        else:
            raise Exception("Biometric login prompt not found")