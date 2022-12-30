import os
import time
import win10toast

# Set the path to the downloads folder 
downloads_folder = os.path.expanduser("~\\Downloads")

# Set the maximum age of the files to delete (in seconds)
max_age = 3600  # 1 hour

# Create a toast notification object
toast = win10toast.ToastNotifier()

while True:
    # Get a list of the files in the downloads folder
    files = os.listdir(downloads_folder)
    for file in files:
        # Get the full path to the file
        file_path = os.path.join(downloads_folder, file)
        # Get the age of the file (in seconds)
        age = time.time() - os.path.getmtime(file_path)
        # Check if the file is older than the maximum age
        if age > max_age:
            # Delete the file
            os.remove(file_path)
            # Show a toast notification to the user
            toast.show_toast("File Deleted", f"Deleted {file}", duration=5)
    # Sleep for a short period of time before checking for more files
    time.sleep(10)
