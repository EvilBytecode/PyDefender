import subprocess

def GraphicsCardCheck():
    try:
        cmd = subprocess.Popen(['wmic', 'path', 'win32_VideoController', 'get', 'name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        gpu_output, err = cmd.communicate()

        if err:
            print(f"Error executing command: {err.decode('utf-8').strip()}")
            return False
        
        if b"vmware" in gpu_output.lower():
            return True
        else:
            return False
    
    except Exception as e:
        print(f"Error in GraphicsCardCheck: {e}")
        return False
