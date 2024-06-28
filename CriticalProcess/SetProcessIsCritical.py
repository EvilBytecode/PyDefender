import ctypes

def set_process_critical():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:
        ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
        return True
    else:
        return False