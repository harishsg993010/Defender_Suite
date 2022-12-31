import os
import psutil
import time

# Set the names of the processes to whitelist
whitelist = [
    "notepad.exe",
    "calc.exe",
]

# Set the names of the LOLBin files
lolbins = [
    "regsvr32.exe",
    "certutil.exe",
    "bitsadmin.exe",
    "certreq.exe",
    "cscript.exe",
    "csc.exe",
    "dnscmd.exe",
    "fpcutil.exe",
    "installutil.exe",
    "mshta.exe",
    "msiexec.exe",
    "msxsl.exe",
    "net.exe",
    "net1.exe",
    "nslookup.exe",
    "powershell.exe",
    "rasautou.exe",
    "reg.exe",
    "regedit.exe",
    "schtasks.exe",
    "sc.exe",
    "taskkill.exe",
    "tasklist.exe",
    "vssadmin.exe",
    "wmic.exe",
]

while True:
    # Get a list of all running processes
    processes = psutil.process_iter()
    for process in processes:
        try:
            # Check if the process is not on the whitelist
            if process.name() not in whitelist:
                # Get the list of open files for the process
                open_files = process.open_files()
                for file in open_files:
                    # Check if the process is accessing a LOLBin file
                    if file.path in lolbins:
                        # Kill the process
                        process.kill()
        except Exception:
            pass
    # Sleep for a short period of time before checking for more processes
    time.sleep(10)
