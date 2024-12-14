# README

## Overview
This Python script retrieves device information from an Android emulator using ADB (Android Debug Bridge) and sends it to a Flask server via an HTTP POST request.

---

## Prerequisites

### 1. **Python Environment**
   - Ensure Python 3.7+ is installed.
   - Install the required libraries by running:
     ```bash
     pip install requests
     ```

### 2. **ADB Setup**
   - Install Android SDK Platform Tools.
   - Add the ADB binary to your system's PATH.

### 3. **Flask Backend**
   - Ensure the Flask backend is running on the configured URL (`http://127.0.0.1:5000/postApp` by default). For setup instructions, refer to the backend's README file.

---

## How to Run

### 1. **Start the Emulator**
   - Launch your Android emulator with ADB.
   - Use the following command to check connected devices:
     ```bash
     adb devices
     ```
     Ensure your emulator appears in the list.

### 2. **Run the Script**
   - Execute the script using:
     ```bash
     python script_name.py
     ```

### 3. **Verify the Backend Response**
   - Check the console for the server response to ensure data was sent successfully.
   - Expected response:
     - **200 OK**: Data sent successfully.
     - Any other status code indicates an issue with the server or request.

---

## Troubleshooting

### Common Issues
1. **ADB Not Recognized**
   - Ensure ADB is installed and added to PATH.
   - Test ADB with:
     ```bash
     adb version
     ```

2. **Emulator Not Found**
   - Start the emulator and ensure it appears in the list using:
     ```bash
     adb devices
     ```

3. **Connection Issues**
   - Verify the Flask server is running and accessible at the specified URL.
   - Ensure the correct port (`5000` by default) is open.

---

## Script Workflow
1. Retrieves device information using ADB commands:
   - **Device ID**
   - **OS Version**
   - **Device Model**
   - **Manufacturer**

2. Sends the retrieved information to the Flask backend via a POST request.

---

## Notes
- Modify the `server_url` variable in the script to point to your Flask server if it differs from the default URL.
- Adjust the sleep time (`time.sleep(10)`) if your emulator requires more time to boot.

