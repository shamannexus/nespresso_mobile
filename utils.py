import subprocess
from const import ApkData


def launch_app():
    """Launches the Nespresso app using ADB."""
    launch_command = f"{ApkData.adb_path} shell am start -n {ApkData.app_package}/{ApkData.app_activity}"
    subprocess.run(launch_command, shell=True, check=True)


def close_app():
    """
    Closes the Nespresso app using ADB.
    First close app and then remove it from the tray
    """
    force_stop_command = f"{ApkData.adb_path} shell am force-stop {ApkData.app_package}"
    kill_command = f"{ApkData.adb_path} shell am kill {ApkData.app_package}"

    subprocess.run(force_stop_command, shell=True, check=True)
    subprocess.run(kill_command, shell=True, check=True)


def reopen_app():
    """Restarts the Nespresso app by force-stopping and then launching it again."""
    force_stop_command = f"{ApkData.adb_path} shell am force-stop {ApkData.app_package}"
    subprocess.run(force_stop_command, shell=True, check=True)
    launch_app()

