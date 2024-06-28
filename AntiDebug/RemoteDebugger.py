import ctypes

kernel32 = ctypes.windll.kernel32

def CheckRemoteDebugger():
    process_handle = kernel32.GetCurrentProcess()
    is_debugger_detected = ctypes.c_int(0)
    kernel32.CheckRemoteDebuggerPresent(process_handle, ctypes.byref(is_debugger_detected))
    return is_debugger_detected.value != 0