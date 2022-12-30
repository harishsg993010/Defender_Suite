import subprocess
import time
import win10toast

# Create a toast notification object
toast = win10toast.ToastNotifier()

while True:
    # Get a list of all scheduled tasks
    tasks = subprocess.run(
        ["schtasks", "/query", "/fo", "csv"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.decode("utf-8").strip().split("\n")[1:]
    for task in tasks:
        # Parse the task name and status from the task information
        task_info = task.split(",")
        task_name = task_info[0].strip('"')
        task_status = task_info[1].strip('"')
        # Check if the task is enabled
        if task_status == "Ready":
            # Delete the scheduled task
            subprocess.run(["schtasks", "/delete", "/f", "/tn", task_name])
            # Show a toast notification to the user
            toast.show_toast("Task Deleted", f"Deleted {task_name}", duration=5)
    # Sleep for a short period of time before checking for more tasks
    time.sleep(10)
