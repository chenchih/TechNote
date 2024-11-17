## Python Path Operations (pathlib)

In this note I want to show using pathlib, however you can also use the os module to establish it. 

> import module: `import pathlib, os`

Pathlib is module that allow you to check your full path location, filter specific file or folder. There is also another alternative module which use like `os` module. 

In this note will cover:
- check current pathlib`
- check file and folder in current directory
- rename, delete file or folder

## Path Displaying 
This section will show your current full path location, and list file files. 

### 1. Displaying and Navigating Paths

- Show current directory path
This allow you see what your full path of your current location, which is like the command `pwd`. This is often use if you want to assign to full path location. 
```
import os
from pathlib import Path
print(Path.cwd())  # Show your current path as a string
print(os.getcwd())
```
- iterate throught current path and list file and directory 
This code is like the command you use `dir` or `ls -al` which is list of the files and subfolders contained in a folder.

```
#using pathlib
for p in Path().iterdir():
    print(p)
```
There's also another old way you can use the `os.listdir()` also have the same effect
```
#using os module
os.listdir() # list current path folder and files`
os.listdir(target_path) #list specify path folder and files
```


### 2. Path Object File Extensions

You can use below to display your file extension name or just show file name. 

> show the file/directory **with extension name**: `.suffix`
> show the file/directory **without extension name**: `.suffix`

```
#  Create Path object file or folder
my_dir = Path("directory_1")
my_file = Path("file_1.txt")

#Print the file with extension name
print(my_dir.suffix)  # 
print(my_file.suffix)  # .txt

#Get Filename without extension name
print(my_dir.stem)#directory_1
print(my_file.stem) #file_1
```


### 3. Combining and Creating Paths

Using combine path location with these method

-	Combine Paths
```
newfile = my_dir / "newfile"
print(newfile)
#directory_1\newfile
```
-	Using `joinpath` as an Alternative
```
newfile = my_dir.joinpath("newfile.txt")
print(newfile)
#directory_1\newfile.txt
```


### 4. Checking File Existence

Using this to check your file exist or not
```
print(my_dir.exists())  # Check if directory exists
print(my_file.exists())  # Check if file exists
print(newfile.exists())  # Check if newfile exists
```

### 5. Absolute and Relative Paths

-	Parent Directories
```
print(my_dir.parent) #.
print(newfile.parent)#directory_1
print(newfile.parent.parent)#.
```
It will show `.` when the file is in the current directory (relative to where your script is running or the current working directory).  For example, if you are running the script in  `C:\pathlib_test`, then `run my_dir.parent` it will show `.`.You can see `newfile.parent` it will show `directory_1`, because newfile parent is `directory_1` 
However, `newfile.parent` will show directory_1 if newfile was defined with a path like "directory_1/file_1.txt". In this case, the parent of newfile is explicitly set to directory_1.

-	Absolute Paths
```
print(my_dir.absolute())#C:\pathlib_test\directory_1
print(newfile.absolute())#C:\pathlib_test\directory_1\newfile.txt
```

-	Using resolve()
```
p = Path("..").resolve()  # Get full path of the parent directory
print(p) #C:\
```

### 6. User Home Directory Access
```
p = Path("~/Pictures").expanduser()  # Access user’s home directory
print(p)

p = Path.home() / "Picture"  # Get path to user's Picture directory
print(p)

```
## Searching and Opening Files

### Glob and rglob: 
-	Using glob for Case-Sensitive Search
```
dotfiles = Path.home() / "test"
for p in dotfiles.glob("*vscode*"):
    print(p)
```
-	Recursive Search with rglob
```
for p in dotfiles.rglob("*.txt"):
    print(p)
```

### Opening and reading Files

-	Open a File with pathlib
```
dotfiles = Path.home() / "Data" / "titanic.csv"
with dotfiles.open() as f:
    print(f.read())
```

- Traditional File Open using with 
```
with open(dotfiles) as f:
    print(f.read())
```


## Limitations of pathlib
## Directory Creation and Removal

-	Create Directory
```
p = Path("TempDir")
p.mkdir()  # Create directory, error if it exists
```

-	Create Directory with Subdirectories
```
p = Path("TempDir/subdir")
p.mkdir(parents=True)
```

-	Remove Directory
```
p.rmdir() # Remove empty directory
```


### File Creation, Rename, and Delete

-	Create File
```
p = Path("TempDir.txt")
p.touch()
```

-	Rename or Replace Files
```
p.rename("hello.txt")  # Rename file
p.replace("hello_2.txt")  # Replace file
```

-	Delete File
```
p.unlink()
```
