import subprocess
import logging
import time

# Configure logging
logging.basicConfig(filename="emulator_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def start_emulator(avd_name):
    try:
        # Check if the AVD exists
        result = subprocess.run(["emulator", "-list-avds"], capture_output=True, text=True)
        avds = result.stdout.strip().split("\n")
        
        if avd_name not in avds:
            logging.error(f"AVD '{avd_name}' not found.")
            print(f"AVD '{avd_name}' not found.")
            return
        
        # Start the emulator
        logging.info(f"Starting emulator '{avd_name}'...")
        subprocess.Popen(["emulator", "-avd", avd_name])  # Non-blocking call
        logging.info(f"Emulator '{avd_name}' started.")
        print(f"Emulator '{avd_name}' started.")
        
        # Wait for emulator to boot up
        logging.info("Waiting for emulator to boot...")
        time.sleep(30)  # Adjust the time based on your system's emulator startup time
        logging.info("Emulator is ready.")

    except Exception as e:
        logging.error(f"Error starting emulator: {e}")
        print(f"Error: {e}")

def install_apk(apk_path):
    try:
        # Install the APK on the running emulator
        logging.info(f"Installing APK from: {apk_path}...")
        result = subprocess.run(["adb", "install", apk_path], capture_output=True, text=True)

        if result.returncode == 0:
            logging.info("APK installed successfully.")
            print("APK installed successfully.")
        else:
            logging.error(f"Error installing APK: {result.stderr}")
            print(f"Error installing APK: {result.stderr}")
    
    except Exception as e:
        logging.error(f"Error installing APK: {e}")
        print(f"Error: {e}")

def get_system_info():
    try:
        logging.info("Retrieving system information...")

        # Retrieve OS version
        os_version = subprocess.run(["adb", "shell", "getprop", "ro.build.version.release"], capture_output=True, text=True).stdout.strip()
        logging.info(f"OS Version: {os_version}")
        print(f"OS Version: {os_version}")

        # Retrieve device model
        device_model = subprocess.run(["adb", "shell", "getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()
        logging.info(f"Device Model: {device_model}")
        print(f"Device Model: {device_model}")
        # Retrieve device manufacturer
        device_manufacturer = subprocess.run(["adb", "shell", "getprop", "ro.product.manufacturer"], capture_output=True, text=True).stdout.strip()
        logging.info(f"Device Manufacturer: {device_manufacturer}")
        print(f"Device Manufacturer: {device_manufacturer}")

        # Retrieve total and available memory
        meminfo = subprocess.run(["adb", "shell", "cat", "/proc/meminfo"], capture_output=True, text=True).stdout.strip()
        mem_lines = meminfo.split("\n")
        total_memory = next((line for line in mem_lines if "MemTotal" in line), "").split(":")[1].strip()
        available_memory = next((line for line in mem_lines if "MemAvailable" in line), "").split(":")[1].strip()
        logging.info(f"Total Memory: {total_memory}")
        print(f"Total Memory: {total_memory}")
        logging.info(f"Available Memory: {available_memory}")
        print(f"Available Memory: {available_memory}")

        logging.info("System information retrieval complete.")
        print("System information retrieval complete.")

    except Exception as e:
        logging.error(f"Error while retrieving system information: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    avd_name = "MyPhone"  # Replace with your AVD name
    apk_path = "D:\WorkPlace\Projects\SumitGoyal_PythonInternAssignment/weather.apk"  # Replace with the path to your APK file

    start_emulator(avd_name)
    get_system_info()
    install_apk(apk_path)
