import requests
import subprocess
import logging
import json
import time

# Configure logging
#logging.basicConfig(filename="client_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to get device info from the Android emulator using ADB
def get_device_info():
    try:
        # Get device ID
        device_id = subprocess.run(["adb", "devices"], capture_output=True, text=True).stdout.splitlines()[1].split("\t")[0]
        
        # Get OS version, device model, and manufacturer
        os_version = subprocess.run(["adb", "shell", "getprop", "ro.build.version.release"], capture_output=True, text=True).stdout.strip()
        device_model = subprocess.run(["adb", "shell", "getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()
        device_manufacturer = subprocess.run(["adb", "shell", "getprop", "ro.product.manufacturer"], capture_output=True, text=True).stdout.strip()

        # Package the mock data in a dictionary
        device_info = {
            "device_id": device_id,
            "os_version": os_version,
            "device_model": device_model,
            "device_manufacturer": device_manufacturer
        }
        
        print("Device info retrieved successfully.")
        return device_info

    except Exception as e:
        print(f"Error while retrieving device info: {e}")
        print(f"Error while retrieving device info: {e}")
        return None

# Function to send data to the Flask server via HTTP POST
def send_data_to_server(data, server_url):
    try:
        print("Sending data to server...")
        response = requests.post(server_url, json=data)
        print(response)
        # Log server's response
        if response.status_code == 200:
            print(f"Server response: {response.json()}")
        else:
            print(f"Error from server: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error while connecting to the server: {e}")

if __name__ == "__main__":
    # Wait for the emulator to boot (if needed)
    time.sleep(10)

    # Flask server URL (Backend)
    server_url = "http://127.0.0.1:5000/postApp"  # Replace with your backend API URL

    # Get device info from the emulator
    device_info = get_device_info()

    if device_info:
        # Send mock data (device info) to the backend server
        send_data_to_server(device_info, server_url)
    else:
        print("No device info to send.")