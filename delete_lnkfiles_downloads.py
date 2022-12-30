import os
import time

# Set the path to the downloads folder
downloads_folder = os.path.expanduser("~\\Downloads")

# Set the maximum age of the files to delete (in seconds)
max_age = 3600  # 1 hour

while True:
    # Get a list of the files in the downloads folder
    files = os.listdir(downloads_folder)
    for file in files:
        # Get the full path to the file
        file_path = os.path.join(downloads_folder, file)
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
    # Sleep for a short period of time before checking for more files
    time.sleep(10)
