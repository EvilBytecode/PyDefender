import ctypes

kernel32 = ctypes.windll.kernel32

def is_debugger_present():
    return kernel32.IsDebuggerPresent() != 0