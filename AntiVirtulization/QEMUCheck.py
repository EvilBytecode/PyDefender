import os

def CheckForQEMU():
    qemu_drivers = ["qemu-ga", "qemuwmi"]
    sys32 = os.path.join(os.getenv("SystemRoot", ""), "System32")

    try:
        detected_drivers = []
        files = os.listdir(sys32)
        for file in files:
            for driver in qemu_drivers:
                if driver in file.lower():
                    detected_drivers.append(driver)
        if detected_drivers:
            return True, detected_drivers
        else:
            return False, None
    except Exception as e:
        return False, f"Error accessing System32 directory: {e}"

    return False, None
