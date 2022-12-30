import os
import psutil
import time

# Set the names of the whitelisted processes
whitelist = ["process1.exe", "process2.exe"]

while True:
    # Get a list of all running processes
    processes = psutil.process_iter()
    for process in processes:
        try:
            # Check if the process has any children
            if len(process.children()) > 0:
                # Get the memory maps of the process and its children
                memory_maps = process.memory_maps() + [
                    child.memory_maps() for child in process.children()
                ]
                # Flatten the list of memory maps
                memory_maps = [item for sublist in memory_maps for item in sublist]
                # Check if any of the memory maps is a DLL being injected into another process
                if any(map.path.endswith(".dll") for map in memory_maps):
                    # Check if the process is not whitelisted
                    if process.name() not in whitelist:
                        # Kill the process
                        process.kill()
        except Exception:
            pass
    # Sleep for a short period of time before checking for more processes
    time.sleep(10)
