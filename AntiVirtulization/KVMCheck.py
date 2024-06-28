import os
import glob

def CheckForKVM():
    bad_drivers_list = ["balloon.sys", "netkvm.sys", "vioinput*", "viofs.sys", "vioser.sys"]
    system32_folder = os.path.join(os.getenv("SystemRoot", ""), "System32")

    for driver in bad_drivers_list:
        files = glob.glob(os.path.join(system32_folder, driver))
        if files:
            return True, None

    return False, None
