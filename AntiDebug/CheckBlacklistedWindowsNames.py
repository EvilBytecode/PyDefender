import ctypes

def CheckTitles():
    user32 = ctypes.windll.user32
    EnumWindows = user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = user32.GetWindowTextW
    GetWindowTextLength = user32.GetWindowTextLengthW
    IsWindowVisible = user32.IsWindowVisible

    forbidden_titles = {
        "proxifier", "graywolf", "extremedumper", "zed", "exeinfope", "dnspy",
        "titanHide", "ilspy", "titanhide", "x32dbg", "codecracker", "simpleassembly",
        "process hacker 2", "pc-ret", "http debugger", "Centos", "process monitor",
        "debug", "ILSpy", "reverse", "simpleassemblyexplorer", "process", "de4dotmodded",
        "dojandqwklndoqwd-x86", "sharpod", "folderchangesview", "fiddler", "die", "pizza",
        "crack", "strongod", "ida -", "brute", "dump", "StringDecryptor", "wireshark",
        "debugger", "httpdebugger", "gdb", "kdb", "x64_dbg", "windbg", "x64netdumper",
        "petools", "scyllahide", "megadumper", "reversal", "ksdumper v1.1 - by equifox",
        "dbgclr", "HxD", "monitor", "peek", "ollydbg", "ksdumper", "http", "wpe pro", "dbg",
        "httpanalyzer", "httpdebug", "PhantOm", "kgdb", "james", "x32_dbg", "proxy", "phantom",
        "mdbg", "WPE PRO", "system explorer", "de4dot", "X64NetDumper", "protection_id",
        "charles", "systemexplorer", "pepper", "hxd", "procmon64", "MegaDumper", "ghidra", "xd",
        "0harmony", "dojandqwklndoqwd", "hacker", "process hacker", "SAE", "mdb", "checker",
        "harmony", "Protection_ID", "PETools", "scyllaHide", "x96dbg", "systemexplorerservice",
        "folder", "mitmproxy", "dbx", "sniffer", "Process Hacker", "Process Explorer",
        "Sysinternals", "www.sysinternals.com", "binary ninja"
    }


    def foreach_window(hwnd, lParam):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        title = buff.value

        if IsWindowVisible(hwnd) and title.lower() in forbidden_titles:
            return True
        return False

    found_forbidden = EnumWindows(EnumWindowsProc(foreach_window), 0)
    return found_forbidden
