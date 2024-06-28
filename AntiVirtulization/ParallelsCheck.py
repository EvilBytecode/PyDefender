import os
import glob

def CheckForParallels():
    parallels_drivers = ["prl_sf", "prl_tg", "prl_eth"]
    sys32_folder = os.path.join(os.getenv("SystemRoot", ""), "System32")

    try:
        files = os.listdir(sys32_folder)
        for file in files:
            for driver in parallels_drivers:
                if driver in file.lower():
                    return True, None
    except Exception as e:
        return False, f"Error accessing System32 directory: {e}"

    return False, None
