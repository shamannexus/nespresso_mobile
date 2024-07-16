import random
import pytest
from utils import launch_app, close_app, reopen_app


@pytest.mark.usefixtures("adb_install_apk", "appium_driver")
class TestNespressoApp:

    def test_register_and_tried_to_buy_product_with_invalid_card(self, appium_driver, steps_class):
        steps = steps_class(appium_driver)  # Initialize the steps class

        # step 1: Access Nespresso app
        success = steps.handle_app_crash_on_launch()
        assert success, "The app did not open correctly or the crash pop-up is still present."

        # step 2: Allow all the necessary locations permissions
        assert steps.handle_location_permission(action='permanently'), "Location permission was not set"

        # step 3,4: Close the app, Reopen the app to check if the location modal windows is not displayed anymore
        close_app()
        launch_app()
        assert not steps.is_permission_popup_appear(), "Permission Pop still appear but should not"
        # here need to click at any element to get notification pop up
        steps.handle_push_notification_popup()

        # step 5: Register a user and allow biometrics
        # TODO: Allow biometrics is not available on emulator, so was not implemented
        some_random_number = random.randint(1000, 9999)
        random_email = f"test{some_random_number}@mailinator.com"
        assert steps.register_new_user(random_email), "New user was not registered"

        # log out here needed because if not logged out - then used will be logged in next time when app is opened
        assert steps.log_out(), "User was not logged out"

        # step 6,7: Close the app, Reopen the app and log in using biometrics if applicable
        reopen_app()
        assert steps.log_in(random_email), "Can not log in with created user"

        # step 8: Find the nearest boutique and try to order capsules with an invalid credit card number
        assert steps.order_product(), "Can not order product"
