import winreg

# Set the key and value to disable VBScript execution
key = r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
value = "DisableVBScript"
value_type = winreg.REG_DWORD
value_data = 1

# Set the value in the registry to disable VBScript execution
winreg.SetValueEx(winreg.HKEY_CURRENT_USER, key, value, value_type, value_data)

# Print a message indicating that VBScript has been disabled
print("VBScript execution has been disabled")
