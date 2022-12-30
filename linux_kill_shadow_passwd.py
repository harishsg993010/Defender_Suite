import os
import psutil
import time

while True:
    # Get a list of all running processes
    processes = psutil.process_iter()
    for process in processes:
        try:
            # Get the list of open files for the process
            open_files = process.open_files()
            for file in open_files:
                # Check if the process is accessing the passwd or shadow file
                if file.path == "/etc/passwd" or file.path == "/etc/shadow":
                    # Kill the process
                    process.kill()
        except Exception:
            pass
    # Sleep for a short period of time before checking for more processes
    time.sleep(10)
