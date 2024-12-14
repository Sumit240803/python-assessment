# Emulator Management Script

## Overview

This script automates the management of an Android Virtual Device (AVD), including:

1. Starting a specified AVD emulator.
2. Installing an APK onto the running emulator.
3. Retrieving system information (OS version, device model, manufacturer, memory details).

## Prerequisites

Ensure you have the following installed and configured:

- **Android Studio** (including Android SDK and AVD Manager).
- **ADB (Android Debug Bridge)**, included with Android SDK.
- **Python 3.7+**.

## Script Details

### Files:

- **`emulator_log.txt`**: Log file where execution details are stored.

### Dependencies:

The script uses the following standard Python modules:

- `subprocess`
- `logging`
- `time`

## Setup Instructions

1. Clone or Download the Repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure the `adb` command is in your system's PATH. To verify:

   ```bash
   adb version
   ```

   If not, add it by updating your environment variables to include the SDK platform-tools directory.

3. Update the script with your configuration:

   - **`avd_name`**: Replace with the name of your AVD (e.g., `"MyPhone"`).
   - **`apk_path`**: Replace with the path to your APK file (e.g., `"D:\WorkPlace\Projects\weather.apk"`).

4. Install Python dependencies (optional for virtual environment):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. Run the script:

   ```bash
   python script.py
   ```

## Script Workflow

1. **Start Emulator**:

   - Validates the specified AVD.
   - Starts the emulator using `emulator -avd <AVD_NAME>`.
   - Logs the emulator startup process.

2. **Retrieve System Information**:

   - Fetches OS version, device model, manufacturer, and memory details via ADB shell commands.

3. **Install APK**:

   - Installs the specified APK file onto the running emulator using `adb install`.

## Example Commands

- **Start Emulator**:

  ```bash
  emulator -avd MyPhone
  ```

- **Check Running AVDs**:

  ```bash
  adb devices
  ```

- **Install APK**:

  ```bash
  adb install <apk_path>
  ```

- **Retrieve System Properties**:

  ```bash
  adb shell getprop ro.build.version.release
  adb shell getprop ro.product.model
  adb shell getprop ro.product.manufacturer
  ```

- **View Memory Info**:

  ```bash
  adb shell cat /proc/meminfo
  ```

## Troubleshooting

- Ensure the AVD name is correct by listing available AVDs:

  ```bash
  emulator -list-avds
  ```

- If the emulator doesn't start, check your Android SDK installation and ensure `emulator` is in the PATH.

- If `adb` commands fail, verify that the emulator is running and properly connected:

  ```bash
  adb devices
  ```

## License

This project is licensed under the MIT License.

