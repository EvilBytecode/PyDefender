import subprocess

def PluggedIn():
    try:
        usbcheckcmd = subprocess.Popen(['reg', 'query', 'HKLM\\SYSTEM\\ControlSet001\\Enum\\USBSTOR'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        outputusb, err = usbcheckcmd.communicate()
        if err:
            return False

        usblines = outputusb.decode('utf-8').split("\n")
        pluggedusb = 0
        for line in usblines:
            if line.strip().startswith("HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Enum\\USBSTOR"):
                pluggedusb += 1

        if pluggedusb > 0:
            return True
        else:
            return False
    
    except Exception as e:
        print(f"Debug Check: Error running reg query command: {e}")
        return False
