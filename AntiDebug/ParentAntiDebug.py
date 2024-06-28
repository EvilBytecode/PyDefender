import ctypes,os,pathlib,sys

PROCESS_QUERY_INFORMATION = 0x0400
MAX_PATH = 260 

class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("Reserved1", ctypes.c_void_p),
        ("PebBaseAddress", ctypes.c_void_p),
        ("Reserved2", ctypes.c_void_p * 2),
        ("UniqueProcessId", ctypes.c_ulong),
        ("InheritedFromUniqueProcessId", ctypes.c_void_p)
    ]

ntdll = ctypes.WinDLL("ntdll.dll")
ntquery = ntdll.NtQueryInformationProcess
ntquery.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(PROCESS_BASIC_INFORMATION), ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]

def NtQueryProc(handle, class_type):
    proc_basic_info = PROCESS_BASIC_INFORMATION()
    return_length = ctypes.c_uint32()
    status = ntquery(handle, class_type, ctypes.byref(proc_basic_info), ctypes.sizeof(proc_basic_info), ctypes.byref(return_length))
    if status != 0x0:
        raise ctypes.WinError(ctypes.get_last_error())
    return proc_basic_info

def QueryImageName(handle):
    name_buffer = ctypes.create_unicode_buffer(MAX_PATH)
    size = ctypes.c_uint32(MAX_PATH)
    if not ctypes.windll.kernel32.QueryFullProcessImageNameW(handle, 0, name_buffer, ctypes.byref(size)):
        raise ctypes.WinError(ctypes.get_last_error())
    return name_buffer.value

def CurrentProcName():
    return pathlib.Path(os.path.abspath(sys.argv[0])).name

def ParentAntiDebug():
    try:
        current_process = ctypes.windll.kernel32.GetCurrentProcess()
        proc_info = NtQueryProc(current_process, 0)
        parent_process = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, proc_info.InheritedFromUniqueProcessId)
        if not parent_process:
            raise ctypes.WinError(ctypes.get_last_error())
        parent_process_name = QueryImageName(parent_process)
        ctypes.windll.kernel32.CloseHandle(parent_process)
        if not (parent_process_name.endswith("explorer.exe") or parent_process_name.endswith("cmd.exe")):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False