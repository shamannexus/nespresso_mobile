import pytest
import subprocess
from appium_driver import AppiumDriver
from const import ApkData


@pytest.fixture(scope="module")
def adb_install_apk():
    """Fixture to install the APK using adb before the tests and uninstall after."""
    install_command = f"{ApkData.adb_path} install {ApkData.apk_path}"
    subprocess.run(install_command, shell=True, check=True)
    yield
    uninstall_command = f"{ApkData.adb_path} uninstall {ApkData.app_package}"
    subprocess.run(uninstall_command, shell=True, check=True)


@pytest.fixture(scope="module")
def appium_driver():
    """Fixture to provide an instance of AppiumDriver for tests."""
    driver_instance = AppiumDriver()
    yield driver_instance
    driver_instance.quit()
