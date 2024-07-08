# Nespresso App Automated Tests

This repository contains automated tests for the Nespresso mobile application using Appium and pytest.

## Project Structure

- **appium_driver**: Contains the `AppiumDriver` class that manages the Appium interactions and configurations.
- **config**: Contains the appium config to connect to the device.
- **const**: Defines constants used throughout the project, including locators (`Locators`), apk (`ApkData`) and user data (`UserData`).
- **conftest.py**: Contains pytest fixtures (`adb_install_apk` and `appium_driver`) used for test setup and teardown.
- **requirements.txt**: Lists Python dependencies required for the project.
- **steps**: Contains `NespressoAppSteps.py` which defines high-level steps or actions for interacting with the Nespresso app.
- **utils**: Contains utility functions such as `launch_app`, `close_app`, and `reopen_app` for managing app lifecycle.
- **tests**: Contains tests
- 
## Installation

1. **Clone the repository:**
  ```
git clone git@github.com:shamannexus/nespresso_mobile.git
  ```
2. **Set up a virtual environment:**

- Install virtualenv if not already installed:

  ```
  pip install virtualenv
  ```

- Create a new virtual environment:

  ```
  virtualenv venv
  ```

- Activate the virtual environment:

  - On Windows:

    ```
    venv\Scripts\activate
    ```

  - On macOS/Linux:

    ```
    source venv/bin/activate
    ```

3. **Install Python dependencies:**
    ```
    pip install -r requirements.txt
    ```

This will install all necessary Python packages including pytest and Appium-Python-Client.

4. **Set up Appium:**

- Ensure that Node.js and npm are installed on your machine.
- Install Appium globally using npm:

  ```
  npm install -g appium
  ```

- Start the Appium server:

  ```
  appium
  ```

  Make sure the Appium server is running on `http://localhost:4723` or adjust the `appium_port` in `config.py` if using a different port.

5. **Install and configure Android SDK:**

- Download and install Android Studio from [developer.android.com](https://developer.android.com/studio).
- Set up environment variables for Android SDK:
  - `ANDROID_HOME` to the location of your Android SDK installation.
  - Update `PATH` to include the Android SDK tools and platform-tools directories.

6. **Install Nespresso App on the device:**

- Connect your Android device or start an Android emulator.
- Ensure USB debugging is enabled on the device.
- Install the Nespresso APK using adb:

  ```
  adb install packages/android_phone/Nespresso_3.35.5_APKPure.apk
  ```
  
## Running Tests

- **Run the test file:**
  ```
  cd tests/ 
  pytest test_nespresso_app.py
  ```
