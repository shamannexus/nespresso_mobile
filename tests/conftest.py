import pytest
import subprocess
from appium_driver import AppiumDriver
from const import ApkData, IpaData
from config import android_device_info, ios_device_info


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android", help="Platform to run tests on: android or ios")


@pytest.fixture(scope="module")
def adb_install_apk(request):
    platform = request.config.getoption("--platform")
    if platform == "android":
        # Install the APK using adb for Android
        install_command = f"{ApkData.adb_path} install {ApkData.apk_path}"
        subprocess.run(install_command, shell=True, check=True)
        yield
        # Uninstall the app after tests
        uninstall_command = f"{ApkData.adb_path} uninstall {ApkData.app_package}"
        subprocess.run(uninstall_command, shell=True, check=True)
    elif platform == "ios":
        # Install the IPA using ios-deploy for iOS
        install_command = f"ios-deploy --bundle {IpaData.ipa_path}"
        subprocess.run(install_command, shell=True, check=True)
        yield
        # Uninstall the app after tests if necessary
        uninstall_command = f"ideviceinstaller -U {IpaData.app_package}"
        subprocess.run(uninstall_command, shell=True, check=True)
    else:
        yield


@pytest.fixture(scope="module")
def appium_driver(request):
    platform = request.config.getoption("--platform")
    if platform == "android":
        driver_instance = AppiumDriver(android_device_info)
    elif platform == "ios":
        driver_instance = AppiumDriver(ios_device_info)
    else:
        raise ValueError("Unsupported platform specified")
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="module")
def steps_class(request):
    platform = request.config.getoption("--platform")
    if platform == "android":
        from steps.android_steps import AndroidNespressoAppSteps
        return AndroidNespressoAppSteps
    elif platform == "ios":
        from steps.ios_steps import IosNespressoAppSteps
        return IosNespressoAppSteps
    else:
        raise ValueError("Unsupported platform specified")
