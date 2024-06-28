import os

def RecentFileActivityCheck():
    try:
        recdir = os.path.join(os.getenv('APPDATA'), 'microsoft', 'windows', 'recent')
        files = os.listdir(recdir)
        if len(files) < 20:
            return True, None
    except Exception as e:
        return False, f"Debug Check: Error reading recent file activity directory: {e}"
    
    return False, None
