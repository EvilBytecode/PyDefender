import ctypes

kernel32 = ctypes.windll.kernel32
getTickCount = kernel32.GetTickCount
getTickCount.restype = ctypes.c_ulong

def GetUptimeInSeconds():
    uptime = getTickCount()
    return int(uptime / 1000)

def CheckUptime(durationInSeconds):
    uptime = GetUptimeInSeconds()
    if uptime < durationInSeconds:
        return True, None
    else:
        return False, None
