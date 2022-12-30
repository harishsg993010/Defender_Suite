import os
import time

# Set the root directory to start the scan from
root_dir = "C:\\"

# Set the maximum age of the files to delete (in seconds)
max_age = 3600  # 1 hour

while True:
    # Walk the directory tree and get a list of all the files
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Get the full path to the file
            file_path = os.path.join(root, file)
            # Check if the file is a Windows shortcut or .iso file
            if file.endswith(".lnk") or file.endswith(".iso"):
                # Check if the file has the MOTW flag set
                if os.lstat(file_path).st_file_attributes & 0x100:
                    # Get the age of the file (in seconds)
                    age = time.time() - os.path.getmtime(file_path)
                    # Check if the file is older than the maximum age
                    if age > max_age:
                        # Delete the file
                        os.remove(file_path)
    # Sleep for a short period of time before scanning again
    time.sleep(10)
