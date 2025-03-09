import subprocess

# Access the output, Capture the output of the 'echo' command
result = subprocess.run(['echo', 'Hello, World!'], shell=True, capture_output=True, text=True)
#subprocess.run(['rm', 'inputs.txt'], shell=True, executable="C:\\Program Files\\Git\\bin\\bash.exe")


# Remove trailing newline with .strip()
print("Standard Output:", result.stdout.strip())
print("Standard Error:", result.stderr.strip())

# Return code
print("Return Code:", result.returncode)  # Expected: 0 (Success)
error_result = subprocess.run(['wrong_command'], shell=True, capture_output=True, text=True)
print("Return Code:", error_result.returncode)# # Expected: Non-zero (Error)

