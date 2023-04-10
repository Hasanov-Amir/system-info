import subprocess
import socket
import time
import os


__all__ = (
    "installed_programs",
    "ip_address",
    "rdp",
    "os_battery_and_time",
    "ms_defender_status",
    "empty_dirs",
    "languages_list",
    "mac",
    "hostname"
)


def installed_programs():
    out = str(subprocess.check_output('wmic product get name', shell=True))

    # filter, validate and split the result
    out = [f"{index + 1}. {i.strip()}" for index, i in enumerate(out.replace('\\r', '').split('\\n')) if len(i) > 2][1:]

    return out


def ip_address():
    # get ip from hostname
    # echo ls %USERDNSDOMAIN%|nslookup
    ip = socket.gethostbyname(socket.gethostname())

    return [f"Ip: {ip}"]


def rdp():
    # https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/troubleshoot/rdp-error-general-troubleshooting
    # fDenyTSConnections
    command = "Get-ItemProperty hklm:\\System\\CurrentControlSet\\Control\\'Terminal Server'"
    out = str(subprocess.check_output(f"powershell.exe {command}", shell=True))

    # split the result
    out = [i.strip() for i in out.replace('\\r', '').split('\\n')]

    rdp_option = None

    for i in out:
        if "fDenyTSConnections" in i:
            rdp_option = int(i[-1])
            # print(f"\n{i}")
            break

    if rdp_option == 1:
        return [f"fDenyTSConnections{rdp_option}\nRemote Desktop Protocol is Disabled"]
    else:
        return [f"fDenyTSConnections{rdp_option}\nRemote Desktop Protocol is Enabled"]


def os_battery_and_time():
    # wmic os get LocalDateTime /value
    seconds = time.time()
    tm = time.localtime(seconds)

    # WMIC PATH Win32_Battery Get EstimatedChargeRemaining
    battery = str(subprocess.check_output("wmic path Win32_Battery get EstimatedChargeRemaining"))\
        .replace('\\r', '')\
        .replace('\\n', '').strip()

    return [f"Time: {tm.tm_hour}:{tm.tm_min}\nBattery:{battery[26:30]}%"]


def ms_defender_status():
    # Get-MpComputerStatus
    out = str(subprocess.check_output("powershell.exe Get-MpComputerStatus", shell=True))
    # filter and split the result
    out = [i.strip() for i in out.replace('\\r', '').split('\\n') if len(i) > 2 and ("True" in i or "False" in i)]

    return out


START_DIR = "C:\\"
LS_EMPTY_DIRS = []


def search_empty_dirs(new_dir=START_DIR):
    # check for dirs
    try:
        ls = os.listdir(new_dir)
    except:
        return 0

    # stop if dir is empty
    if len(ls) == 0:
        LS_EMPTY_DIRS.append(new_dir)
        return 0

    for ls_dir in ls:
        # search in new subdir
        search_empty_dirs(new_dir="\\".join([new_dir, ls_dir]))


def empty_dirs():
    # run search
    search_empty_dirs()

    return LS_EMPTY_DIRS


def languages_list():
    # Get-WinUserLanguageList
    out = str(subprocess.check_output("powershell.exe Get-WinUserLanguageList", shell=True))
    # filter, validate and split the result
    out = [i.strip().split(":")[-1] for i in out.replace('\\r', '').split('\\n') if len(i) > 2 and "EnglishName" in i]

    return out


def mac():
    out = str(subprocess.check_output("getmac", shell=True))
    out = [i.strip() for i in out.replace('\\r', '').replace("=", "").split('\\n') if len(i) > 2]
    return out


def hostname():
    out = subprocess.check_output("hostname", shell=True)
    return [out.decode()]
