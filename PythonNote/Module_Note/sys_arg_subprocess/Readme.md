#Understand how to use sys.argv and subprocess

## using sys.argv

It retrieves command-line arguments passed to a script. This is helpful when you want to pass arguments as input without hardcoding the input values in the code.

Run the code by passing two arguments: `python example.py arg1 arg2`

> Output: `['example.py', 'arg1', 'arg2']`

- `sys.argv[0]` is `example.py`.
- `sys.argv[1]` is `arg1`.
- `sys.argv[2]` is `arg2`.

The first element (`sys.argv[0]`) is the name of the script (or its path). Subsequent elements (`sys.argv[1]`, `sys.argv[2]`, etc.) are the additional arguments passed to the script.

### passing argument example


Run code below like this: `py sys_argvSample.py hello`
```
import sys

if __name__ == '__main__':
    print("All arguments:", sys.argv) #All arguments: ['sys_argvSample.py', 'hello']
    if len(sys.argv) < 2:  
        print('no argument')
        sys.exit()
    print(f"sys.argv[0]: {sys.argv[0]}")#sys.argv[0]: sys_argvSample.py
    print(f"sys.argv[1]: {sys.argv[1]}")#sys.argv[1]: hello
```

The script checks if additional arguments are provided by evaluating `len(sys.argv) < 2`. If no arguments are provided, it prints 'no argument' and exits. If arguments are provided, it displays the script name (`sys.argv[0]`) and the value of each subsequent argument based on their index in `sys.argv`.

### use window script to run it 
If you want to run with window batch script you can do like this, it will auto run your python file.

- Create a script `testscript.bat`
```
@echo off
python sys_argvSample.py %*
```

- run the script with argument: `testscript.bat hello`

You can pass an argument string after the script name. 

## using subprocess

`subprocess.run` is a Python function from the subprocess module that allows you to run system commands directly from your Python script. It provides a way to execute shell commands and interact with external programs, such as `FFmpeg`, `Git`, or any other `CLI tool`.

> syntax: 
>> `subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, check=False, timeout=None, text=None)` 

- `args`: A list of the command and its arguments, e.g., [`ls`, `-l`]. Alternatively, a single string if `shell=True`.
- `shell`: If True, runs the command in a shell. (Caution: this can be unsafe with untrusted input.)
- `check`: If `True`, an exception is raised if the command exits with a non-zero status.
- `stdout/stderr`: Where to redirect the output (e.g., subprocess.PIPE to capture it).
- `text`: If True, treats output as a string (instead of bytes).


### Simple example
```
import subprocess

# Run the 'ls -l' command (list files in a directory, long format)
result = subprocess.run(['ls', '-l'], text=True)
print(result)
```
### Capturing Command Output

- `shell=True`: Run command in window
without `shell=True`, Python directly looks for an executable file named `echo` in your system's PATH. Since no such file exists, it fails. The subprocess.run call cannot find the `echo` command on your system. On Windows, echo is a built-in shell command (part of cmd.exe) and is not an executable file.
- `capture_output=True`: Captures `stdout` and `stderr` output
	- `stdout`: Output from the command
	- `stderr`: Error messages (if any) 
	- `returncode`: Exit status of the command that was executed, error return non zero

when you need to process the output of the command in your script instead of printing it directly.

```
import subprocess

# Access the output, Capture the output of the 'echo' command
result = subprocess.run(['echo', 'Hello, World!'], shell=True, capture_output=True, text=True)

# Remove trailing newline with .strip()
print("Standard Output:", result.stdout.strip())
print("Standard Error:", result.stderr.strip())

# Return code
print("Return Code:", result.returncode)  # Expected: 0 (Success)
error_result = subprocess.run(['wrong_command'], shell=True, capture_output=True, text=True)
print("Return Code:", error_result.returncode)# # Expected: Non-zero (Error)
```

### `executable` Run with special command
If you want to run special command with special tool, you can use `executable=` option
```
subprocess.run(['rm', 'inputs.txt'], shell=True, executable="C:\\Program Files\\Git\\bin\\bash.exe")
```

