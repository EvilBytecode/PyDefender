import subprocess

def TriageCheck():
    try:
        result = subprocess.check_output(['wmic', 'diskdrive', 'get', 'model'], text=True)
        if "DADY HARDDISK" in result or "QEMU HARDDISK" in result:
            return True
    except subprocess.CalledProcessError as e:
        print(f"Error running wmic command: {e}")
        return False
    
    return False
