import os
import psutil
import time

while True:
    # Get a list of all running processes
    processes = psutil.process_iter()
    for process in processes:
        try:
            # Check if the process is running the vssadmin command
            if "vssadmin" in process.cmdline():
                # Check if the process is attempting to delete the shadow copies
                if "delete" in process.cmdline() and "shadows" in process.cmdline():
                    # Kill the process
                    process.kill()
        except Exception:
            pass
    # Sleep for a short period of time before checking for more processes
    time.sleep(10)
