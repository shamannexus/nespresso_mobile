from appium.webdriver.common.appiumby import AppiumBy
import os
current_dir = os.path.dirname(os.getcwd())

class ApkData:
    apk_name = "Nespresso_3.35.5_APKPure.apk"
    # apk_location = "../packages/android_phone/"
    # apk_location = "packages/android_phone/"
    apk_location = os.path.join(current_dir, 'packages', 'android_phone/')
    apk_path = apk_location + apk_name

    adb_path = "/home/bogdanshkribliak/Android/Sdk/platform-tools/adb"
    # adb_path = "adb"
    app_package = 'com.nespresso.activities'
    app_activity = 'com.nespresso.ui.activity.LaunchActivity'


class Locators:
    close_alert_button_locator = (AppiumBy.ID, 'android:id/button1')
    confirm_sign_in_btn = (AppiumBy.ID, 'com.nespresso.activities:id/btn_progress')
    pop_up_locator = (AppiumBy.ID, 'com.nespresso.activities:id/parentPanel')
    decline_btn = (AppiumBy.ID, 'android:id/button2')
    account_locator = (AppiumBy.ID, 'com.nespresso.activities:id/tab_title_account')
    create_account_btn = (AppiumBy.ID, 'com.nespresso.activities:id/tv_register')
    web_view_locator = (AppiumBy.CLASS_NAME, "android.webkit.WebView")
    title_locator = (AppiumBy.XPATH, "//*[@id='private-titleCode']")
    first_name_locator = (AppiumBy.XPATH, "//*[@id='personalInfo-firstName']")
    last_name_locator = (AppiumBy.XPATH, "//*[@id='personalInfo-lastName']")
    email_locator_when_register = (AppiumBy.XPATH, "//*[@id='email']")
    password_locator_when_register = (AppiumBy.XPATH, "//*[@id='password']")
    email_locator_when_log_in = (AppiumBy.ID, "com.nespresso.activities:id/et_email")
    password_locator_when_log_in = (AppiumBy.ID, "com.nespresso.activities:id/et_password")
    continue_registration_btn_locator = (AppiumBy.XPATH, "//*[@text='Continue registration']")
    address_line_1_locator = (AppiumBy.XPATH, "//*[@id='addressInfo-firstAddressLine']")
    town_locator = (AppiumBy.XPATH, "//*[@id='addressInfo-townCity']")
    postcode_locator = (AppiumBy.XPATH, "//*[@id='addressInfo-postcode']")
    phone_locator = (AppiumBy.XPATH, "//*[@id='addressInfo-phone1-number']")
    skip_btn_locator = (AppiumBy.ACCESSIBILITY_ID, "Skip and register next time")
    complete_registration_btn_locator = (AppiumBy.XPATH, "//*[@text='Complete registration']")
    sign_out_btn = (AppiumBy.ID, 'com.nespresso.activities:id/btn_signout')
    sign_out_confirm_btn = (AppiumBy.ID, 'android:id/button1')
    sign_in_btn = (AppiumBy.ID, 'com.nespresso.activities:id/btn_signin')
    shop_locator = (AppiumBy.ID, 'com.nespresso.activities:id/tab_title_shop')
    first_available_product_locator = (AppiumBy.XPATH,
                                       '(//android.widget.CheckedTextView[@resource-id="com.nespresso.activities:id/product_add_button"])[1]')
    one_item_locator = (AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="1"]')
    basket_locator = (AppiumBy.ID, 'com.nespresso.activities:id/tab_title_basket')
    continue_btn_locator = (AppiumBy.ID, 'com.nespresso.activities:id/button_checkout_basket')
    boutique_radio_btn_locator = (AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="com.nespresso.activities:id/radio_button"])[3]')
    gps_btn_locator = (AppiumBy.ID, 'com.nespresso.activities:id/bt_gps')
    first_shop_locator = (AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.nespresso.activities:id/choose"])[1]')
    credit_card_radio_btn_locator = (AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="com.nespresso.activities:id/radio_button"])[1]')
    credit_card_number_locator = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.nespresso.activities:id/edit_text" and @text="Credit Card number *"]')
    ccv_code_locator = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.nespresso.activities:id/edit_text" and @text="CVV / CVC code *"]')
    grant_dialog = 'com.android.permissioncontroller:id/grant_dialog'
    permission_permanently_button = 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
    permission_one_time_button = 'com.android.permissioncontroller:id/permission_allow_one_time_button'
    permission_deny_button = 'com.android.permissioncontroller:id/permission_deny_button'


class UserData:
    option_text = "Mr."
    first_name = "Test"
    last_name = "Test"
    password = "12345678Test"
    address_line_1 = "test_address"
    town = "Montgomery"
    postcode = "36109"
    phone_number = "1111111111"
    credit_card_number = '1111 1111 1111 1111'
    ccv_code = '111'
