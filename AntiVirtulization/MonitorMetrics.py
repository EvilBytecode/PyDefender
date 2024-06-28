import ctypes

def IsScreenSmall():
    try:
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0) 
        height = user32.GetSystemMetrics(1)

        is_small = width < 800 or height < 600
        return is_small, None
    except Exception as e:
        return False, f"Error checking screen size: {e}"
