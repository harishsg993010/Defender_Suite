import os
import psutil
import time
import winreg

# Set the names of the programs to disable
blocklist = [
    "reg.exe",
    "cmd.exe",
    "powershell.exe",
    "certutil.exe",
    "schtasks.exe",
    "mshta.exe",
    "InstallUtil.exe",
    "AppInstaller.exe",
    "bash.exe",
    "wsl.exe",
    "certoc.exe",
    "bitsadmin.exe",
    "certreq.exe",
    "Cmstp.exe",
    "Csc.exe",
    "Cscript.exe",
    "CustomShellHost.exe",
    "Dnscmd.exe",
    "finger.exe",
    "msdt.exe",
    "regsvr32.exe",
    "wsl.exe",
]

# Set the key and value for the Image File Execution Options key
key = winreg.HKEY_LOCAL_MACHINE
value = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"

while True:
    # Open the Image File Execution Options key
    with winreg.OpenKey(key, value, 0, winreg.KEY_WRITE) as key:
        # Get a list of all subkeys
        subkeys = winreg.EnumKey(key, 0)
        # Iterate over the subkeys
        for subkey in subkeys:
            # Check if the subkey is in the blocklist
            if subkey in blocklist:
                # Set the Debugger value to an empty string to disable the program
                winreg.SetValueEx(key, subkey, 0, winreg.REG_SZ, "")
