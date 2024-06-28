import os
import glob

def VMArtifactsDetect():
    bad_file_names = ["VBoxMouse.sys", "VBoxGuest.sys", "VBoxSF.sys", "VBoxVideo.sys", "vmmouse.sys", "vboxogl.dll"]
    bad_dirs = [r'C:\Program Files\VMware', r'C:\Program Files\oracle\virtualbox guest additions']

    system32_folder = os.getenv("SystemRoot", "") + r'\System32'
    try:
        files = glob.glob(os.path.join(system32_folder, "*"))
    except Exception as e:
        print(f"Error accessing System32 folder: {e}")
        return False

    badfileslower = [name.lower() for name in bad_file_names]

    for file_path in files:
        file_name = os.path.basename(file_path).lower() 
        if file_name in badfileslower:
            return True

    bad_dirs_lower = [dir.lower() for dir in bad_dirs]

    for bad_dir in bad_dirs_lower:
        if os.path.exists(bad_dir):
            return True

    return False
