# Cheat Sheet
Record Cheat Sheet Note
## Update Record
- 2025/3/10:
	- adding remove branch, remove remote branch, fetch -- plume
- 2025.2.24: 
	- update git push setting
	- window shortcut	
## Git Command 

- `git reset ` -> change to `git restore`
- `git status`  -> change to `git status -sb`
- `git pull` -> change to `git pull --rebase`
- `git checkout` -> change to `git switch`
- `git stash` -> change to `git worklist`
- `git merge` ->  change to `git rebase`

### Git push and upstream setting

#### setting git push:`upsteam` and `-u`
The point of setting upstream is to then simply use `git push` in the future, instead of entering full remote name.

- `git branch --set-upstream-to=origin/<branchname>`
	- This command only establishes the upstream tracking. It tells your local branch "This remote branch (origin/branchname) is where I should be pushing to by default."
	
- `git push -u origin <branchname>`
	- It pushes your local branch to the remote branch (origin/branchname).
	- It sets the upstream tracking for your local main branch to origin/main
	- summary: it create upstream tracking and push local to remote. 
	
#### Check tracking status
- `git branch -vv` : Checking Upstream tracking Settings
It lists your local branches and shows which remote branch they are tracking, I had use checkout to track local and remote. If I use git pull, it will automatic pull track from remote to local side. 
```
git branch -vv
  main c8c14dd [origin/main: behind 3] adding ocr note, and upload pathlib demo_testfile
* tmp  00f963e [origin/tmp] remove ffmegp exe file
```

#### git push 
- `git push origin main` or `git pull`
	- **Bypassing Upstream**
	- Explicitly telling Git push my current branch to origin/main, regardless of what my upstream setting is
	- This command pushes your local branch to the remote branch (`origin/branchname`).

###  Create, Push and Pull from local to server

- create branch:`git checkout <branch_name>`
- remove local branch: `git branch [-D|-d] <branch_name>`
	- `-d`: checks if the branch has been fully merged into its upstream branch. If it has, it deletes the branch. If not, it will return an error.
	- `-D`: If you want to force deletion (even if it's not fully merged)
- remove remote branch: `git push origin --delete <branch_name>` or `git push origin :<branch_name>`
- git pull: download and merge
```
#better way of using git pull:
git pull #git fetch+git merge
git pull --rebase #use this instead of git pull
#these are other option:
git pull --ff only #only fetch new commit 
git pull -- ff

```

#### Case1: Push remote branch with same and different branch name
Imagine PC1 use at office, and PC2 use at home. 

##### 1.1 PC1 push: both local and remote branch with same name
This example will show using same branch name on both local and remote. 

- Create local `tmp` branch and push to remote branch `tmp` 
Local branch and remote branch use the same name
```
git checkout -b tmp #create and change new branch in local side
git add .
git commit -m <message to commit> 

#Pushes your current local branch to a remote branch with the same name
git push -u origin <remote branch name, ex:tmp>

```
##### 1.2 [Git push] PC1 push: local and remote branch with same different name
Push the local main branch to the remote branch name `tmp`. If `tmp` doesn't exist on the remote, it will auto created.

- Push local `main` branch to remote branch `tmp`(or different remote branch name)
Local branch and remote branch use different name
```
#main branch 
git add .
git commit -m <message to commit> 
#Pushes your local main branch to a remote branch named tmp branch
git push origin main:tmp #Does not set upstream tracking.
```

#### Case2 [Git pull] PC2 pull remote origin/tmp to local tmp branch(auto create it)
This command creates a new local branch tmp that tracks the remote `origin/tmp branch` and switches to it. 
This is PC2 which don't have `tmp` branch in local side, and want to download remote `origin/tmp` data to local side. In PC2 just `case1-1` or `case1-2` create a remote branch `tmp`, if you want the branch to download local branch, just this method. 

```
git fetch --all #will update remote branch list
git checkout -b tmp origin/tmp
git commit -m "commit msg"
git push -u origin tmp
```

you can use the `remote branch -r` to see your updated remote list. 


#### Case3: [Git pull] PC1 pull origin/tmp to local main without create `tmp` or any branch 
In PC2 push to remote tmp, now what if I want to pull down to main branch. 

- > Pull `Remote tmp -> local main branch`
```
method1:
#Fetch the Remote tmp Branch
git fetch origin
#switch to main, in case only main branch can ignoire)
git checkout main
#Merge origin/tmp into main(local)
git merge origin/tmp

#method2: Fetches and merges origin/tmp into the local main branch in a single command.
git pull origin tmp:main
```

### Check Remote branch 
This command will lists your remote-tracking branches 

- `git branch -r`: check the available remote branches
```
 origin/HEAD -> origin/main
  origin/main
  origin/tmp
```
- `git remote show origin`: tells you about the remote repositories themselves (URLs, settings, etc.).
```
* remote origin
  Fetch URL: https://github.com/chenchih/TechNote.git
  Push  URL: https://github.com/chenchih/TechNote.git
  HEAD branch: main
  Remote branches:
    main tracked
    tmp  tracked
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (up to date)
```

#### Remote Tracking Branches
`--prune` is used to clean up  remote-tracking branches in your local repository. When you delete a branch on your GitHub server, Git doesn't automatically remove the corresponding remote-tracking branch from your local repository.



**When using it?**
When you delete a branch on GitHub (or any remote), the corresponding remote-tracking branch in your local repository are old. It still exists locally, but it no longer matches the state of the remote

**Sumamry:**
When you delete a branch on GitHub, you need to use git fetch --prune (or its variations) to remove the stale remote-tracking branch from your local repository.
This command fetches the latest changes from the remote and removes any remote-tracking branches that no longer exist on the remote.

- `git fetch --prune`: remove remote-tracking branches 
	- `git fetch origin --prune`: Specific to the origin remote, working with a single remote
	- `git fetch --prune`: Specific to the default or tracked remote. Unsure which remote you are tracking, and want to prune the remote you are tracking
	- `git fetch --all --prune`: Applies to all configured remotes, working with multiple remotes

if you are working with a repository where origin is your primary remote and most of your branches track origin, then these two commands will produce the same result.
```
# some remote tracking is been remote
PS C:\gitfile\TechNote> git branch -r
  origin/HEAD -> origin/main
  origin/main
  origin/tmp
  origin/tmp_pathlib

# using prune the not exist wil remove 
PS C:\gitfile\TechNote> git fetch --prune
  origin/HEAD -> origin/main
  origin/main
  origin/tmp
```

### git stash
- `git stash`: is a local operation. It does not interact with remote repositories. It is a **temporary** holding area for your **uncommitted changes**.
update from the remote, and then reapply your work.This helps you avoid conflicts during the git pull process. If the remote changes and your local changes affect the same lines in the same file, you will need to manually solve the merge conflicts. 

- commonly use:
	- `git stash`
	- `git stash pop` : apply the changes I made earlier in tmp and apply to it (attempts to merge your stashed changes with the current state of your working directory) and will alert you to any conflicts that arise. **It apply and delete**
	- `git stash apply`: is similar to git stash pop, it **apply and keep**, allow to apply stashed changes repeatedly..
- other option can use:
	- `git stash list`: list multiple stash if you create multiple 
	- `git stash apply stash@{}`: switch to specific stash 
	- `git stash drop stash@{id}`: remove git stash
	- `git clear`: clear all stash

I am editing `test.py`, then there are some new updates on the remote. I need to save my uncommitted changes and perform a git pull to update my local repository with the latest changes from the remote. In this case, I will use git stash to save my uncommitted changes to a temporary location (the stash).

Now, I will use git pull to fetch and merge the latest changes from the remote into my current local branch. After the git pull is complete, I will use git stash pop to reapply the changes I made to test.py before the pull.

### Interactive rebase
interactive rebase `git rebase -i` to modify history you can use these option below:
- `pick` (or p): Use this commit as is.
- `squash` (or s): Combine this commit into the previous commit. You'll get a chance to edit the combined commit message.
- `fixup` (or f): Combine this commit into the previous commit, discarding this commit's log message.
- `reword` (or r): Use this commit, but edit the commit message.
- `drop (or d)`: Remove this commit entirely.


#### squash commit (squeeze multiple commit into one)
If you have long commit history, you can use the squash with interactive rebase command (`git rebase -i`). This method will make history cleaner and easier to follow, especially if many of those commits are small fixes.

Step1: check log `git log --graph --oneline #show log` 
```
git log --graph --oneline #show log 
* f764533 (HEAD -> main) 4/23 update cheatheet 
* 00f963e (origin/tmp) remove ffmegp exe file
* 4f81424 update cheatsheet emoji, and fgmepg
* 30fbb20 adding cheatsheet:git note
```

Step2: squash 00f963e and 4f81424 into 30fbb20: ` git rebase -i 30fbb20^`

The `<commitID>^` for example: 4f81424^ refers to the parent commit of 4f81424, so in the log the parent of 4f81424 is 30fbb20.

When you use `rebase -i` which will go to inactivate mode, which allow you to modify commit. Change the commit you want to squash with `squash`, and save the file.  
```
pick 30fbb20 adding cheatsheet:git note
squash 4f81424 update cheatsheet emoji, and fgmepg
squash 00f963e remove ffmegp exe file
pick f764533 4/23 update cheatheet
```

Step3: check the log again
When you chek the log, you will have realize the orginal commit is been squash. 
After squashed commit will have a brand new and different Git commit ID, please keep in mind. 
```
git log --graph --oneline #show log 
* bb46a24 (HEAD -> main) 4/23 update cheatheet
* c7448f0 adding cheatsheet:git note
* 8d04e9c (origin/main, origin/HEAD) adding git command in cheatsheet
```

Please refer below picture for more detail:
[rebase_squash](img/git_squashcommit.PNG)

#### reword commit(edit your commit msg)
If you want to modify your commit msg, you can use the `reword` like above rebase inactive. Please refer below picture for more detail. 
[rebase_reword](img/git_rewordcommit.PNG)


### check commit log: gitlog 
- `git log --graph --oneline --decorate --all`
- `gitk --all` : (GUI)
- `git log  --pretty=format:"%h %s"`
`%h` is shorthand for hash_id and `%s` shorthand for subjectName[message_name]
```
git log  --pretty=format:"%h %s"
#output
5e923eb to organize note for readme
ce17fb7 adding link to each section of a page, and examples folder
8976dcd adding response model's account normal usage example

git log --pretty=format:%s # first line of the messages

#output
to organize note for readme
adding link to each section of a page, and examples folder
adding response model's account normal usage example
```

- `git log --pretty=format:"%h   %s %C(yellow)(%cr)"`
%C is a shorthand for color
```
 show date behind commit-id and message
```

- git log --oneline --grep="add"


### Undo and recover commit
- `Reset`: Primarily used to move the branch pointer (HEAD) to a specific commit, effectively undoing commits on the current branch. Options like --hard can also discard changes, potentially rewriting history
	- `hard`: Undo everything (commits, staging, working directory) back to the specified point.
	- `soft`: Move back to uncommit (changes are staged, ready to commit again).
	- `mixed(default)`: Move back to unstaged (changes are in the working directory, ready to be staged).
- `restore`:  Used to undo changes in the working directory (unstaged) or to unstage files (move from staging back to working directory). It operates on the current working state and staging area, not directly on committed history
- `revert`: sed to undo a specific commit by creating a new commit that reverses its changes. This preserves the original commit and the history, making it safe for shared branches

#### Case1 git reset: if accident remove commit

Step1: check you log status
```
PS C:\gitfile\testlog> git log --oneline
c153b52 (HEAD) add comment
d0159e4 add python file name testhello
6c097d5 update
aa60785 Revert "modify xx to real name"
44bb243 hello added

```
Step2: accident delete a commit
```
PS C:\gitfile\testlog> git reset --hard d0159e4
HEAD is now at d0159e4 add python file name testhello

#check log again
PS C:\gitfile\testlog> git log --oneline
d0159e4 (HEAD) add python file name testhello
6c097d5 update
```
Step3: reflog to check delete commit id
```
#use reflog to check remove commit
PS C:\gitfile\testlog> git reflog
d0159e4 (HEAD) HEAD@{0}: reset: moving to d0159e4
c153b52 HEAD@{1}: commit: add comment
d0159e4 (HEAD) HEAD@{2}: commit: add python file name testhello
6c097d5 HEAD@{3}: commit: update
```

Step4: recovery d0159e4
```
PS C:\gitfile\testlog> git reset --hard c153b52
#check log again, add comment is been recover
PS C:\gitfile\testlog> git log --oneline
c153b52 (HEAD) add comment
d0159e4 add python file name testhello
6c097d5 update
```
#### Case2 git restore: restore to untrack 

Restore undoing changes in your local, uncommitted work (working directory and staging area). It only operates on the working directory and the staging area, fter commit will not be able to undo. 

It have two method one is to undo your editing file, and another one is adding `staged` option to move back to unstaged. 


- Restore
```
#edit your file add hello to it
PS C:\gitfile\gitdemotest> notepad.exe .\note.txt
#it will undo file to orginal file content
PS C:\gitfile\gitdemotest> git restore .\note.txt
```

- Restore with staged

Create file and stage it
```
PS C:\gitfile\gitdemotest> notepad.exe .\note.txt
PS C:\gitfile\gitdemotest> git add .\note.txt #stage your file
PS C:\gitfile\gitdemotest> git status
On branch master
Changes to be committed: #change to stage
  (use "git restore --staged <file>..." to unstage)
        modified:   note.txt
```

Resore back to unstage:
```
PS C:\gitfile\gitdemotest> git  restore --staged note.txt
PS C:\gitfile\gitdemotest> git status
On branch master
Changes not staged for commit:   #change not staged
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   note.txt
```

#### Case3 git revert: undo commit 

git revert provides a safe way to undo changes because it adds a new commit, instead of remove it. It focuses on **creating a new commit that explicitly reverses the changes introduced by a specific past commit**.

It designed to undo the changes of a commit by creating a new commit that reverses those changes, thereby preserving the history of the repository. It's the safe and recommended way to undo changes in a collaborative environment.

Step1: add and commit file 
```
git init
echo "Initial text" > README.md
git add README.md
git commit -m "initial commit"

# in case this is a typo which we want to undo 
echo "bad update" > README.md
git commit -am "bad update"
```

Check log:
```
PS C:\gitfile\test_revert> git log --oneline
568e132  (HEAD -> master) bad update
7b5b95b ading readme
```

Step2: revert the head which is the typo we want to undo it
```
git revert HEAD

Revert "bad update"

This reverts commit 568e132b11facae397b05902d9234d0739fc06a6.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
# Changes to be committed:
#       modified:   README.md

```

If you want to leave default message just press `wq` to save and exit 

Step3: check log 
```
PS C:\gitfile\test_revert> git log --oneline
1ede0b9 (HEAD -> master) Revert "bad update"
568e132 bad update
7b5b95b ading readme
```
You can see it create a new commit `1ede0b9 (HEAD -> master) Revert "bad update"` instead of removing the `568e132 bad update`. 
using revert will be safer, which preserving commit in the history. This allow you to switch back in future if you want to use. 

#### Case4 reset back to uncommit 
In this example I will show you how to reset back to uncommit status and return back to commit status:
- step2: undo commit(return to step1)
- step3: undo step2 (return to step1)

Step1: add and commit file 
```
git init
echo "Initial text" > README.md
git add README.md
git commit -m "initial commit"

# in case this is a typo which we want to undo 
echo "bad update" > README.md
git commit -am "bad update"
```
Check log:
```
PS C:\gitfile\reset_test> git log --oneline
bf82263 (HEAD -> master) bad update
29938d0 initial commit
```

Step2: undo commit by `reset --soft`
moves the master branch pointer back 
```
PS C:\gitfile\reset_test> git reset --soft HEAD^
PS C:\gitfile\reset_test> git log --oneline
29938d0 (HEAD -> master) initial commit
```

Step3: undo commit by `reset --soft`
In case in you want to undo step2 to orginal place, use `git reflog` to find your git ID

```
PS C:\gitfile\reset_test> git reflog show HEAD
29938d0 (HEAD -> master) HEAD@{0}: reset: moving to HEAD
29938d0 (HEAD -> master) HEAD@{1}: reset: moving to HEAD
29938d0 (HEAD -> master) HEAD@{2}: reset: moving to HEAD
29938d0 (HEAD -> master) HEAD@{3}: reset: moving to HEAD^
```
git reset to step1

```
git reset --hard bf82263

PS C:\gitfile\reset_test> git log --oneline
bf82263 (HEAD -> master) bad update
29938d0 initial commit
```

#### Case5 reset back to unstage
Undoing git reset --soft HEAD^ to go back to the unstaged state

Step1: continue Case4 and check log
```
PS C:\gitfile\reset_test> git log --oneline
bf82263 (HEAD -> master) bad update
29938d0 initial commit
```
Step2: reset to uncommit to stage
```
git reset --soft HEAD^

PS C:\gitfile\reset_test> git log --oneline
29938d0 initial commit

PS C:\gitfile\reset_test> git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```		
Step3 reset to unstage `git reset` or `git reset --mixed` as default
```
PS C:\gitfile\reset_test> git reset
Unstaged changes after reset:
M       README.md

PS C:\gitfile\reset_test> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
```

### Visualize your Git branch graph 
- `git log --graph --oneline --decorate --all`
- `gitk --all` : (GUI)


## PYTHON


### Create virtual env
This is a useful way to isolation your current environment with new environment. Sometimes some pakage might conflict with specfic version and cause not able to install or run.  You can just create a virtual environment with a fresh environment  which will not effect your current environment. 


#### using venv:

- `python3.13 -m venv testbuild`
	
#### using virtualenv: 
- install with pip

- `virtualenv <venv_name>`
When you run virtualenv <venv_name> without specifying a Python interpreter, virtualenv typically uses the Python interpreter that is first in your system's PATH environment variable.

- specific version: `virtualenv -p py -3.12 <venv_name>` 
- Explicitly Specifying the Interpreter Path: 
	- window: `virtualenv -p "C:\path\python3.12\python.exe" <venv_name>`, use `<venv_name>\Scripts\activate` to activate
	- linux: `virtualenv -p "/usr/bin/python3.12" <venv_name>`, use `source <venv_name>/bin/activate` to activate

### Convert python to executable file
Convert your python code to an executable file (`.exe`) which allow to run code in  different environment without install python or pkg

Install pyinstaller pkg: `pip install pyinstaller`

```
#simple convert 
pyinstaller your_script.py
#include icon
pyinstaller --onefile --icon=desktop.ico  xxx.py

```

- Please refer other option command you can use:
	- Single File: `pyinstaller  --onefile  your_script.py`
	- Adding Icons: `pyinstaller --onefile --icon=myicon.ico your_script.py`
	- no console window: `pyinstaller --onefile --windowed your_script.py`
	- Adding Data Files: `pyinstaller --onefile --add-data "data_file.txt;." your_script.py`

- Ico download link:
	- Icon URL: `https://www.flaticon.com/`
	- convert `.png` to `ico`: https://convertio.co/zh/


### Convert python to executable file

Convert your code to executable file in different envirnoment without install package
```
pyinstaller --onefile --icon=desktop.ico  xxx.py
```
- Icon URL: `https://www.flaticon.com/`
- convert `.png` to `ico`: https://convertio.co/zh/



## Window 

### Shortcut command

#### window run window
Press `window+R` to run some shortcut and enter below command:

- Network interface網路連線: `ncpa.cpl`
- check PC HW information: `msinfo32` 
- check services running: `services.msc`
- system setting: `msconfig`
- check window version: `winver`
- open specific or drive: `explorer <path>`, ex: `explorer d:` 
	- also work on `command prompt`
- open home path: `%HOMEPATH%`
- devices management: `devmgmt.msc` checking driver version and install or not  
- firewall setting: `wf.msc`
- remote desktop: `MSTSC`

#### command promopt
- check process: `tasklist  |grep nameapp`
- kill process: 
	- stop process ID: `taskkill /pid <process ID> /f`
	- stop python: `taskkill /IM python.exe /f` 
	- stop cmd: `Get-Process -Name "cmd" | Stop-Process`
- check recursive of working directory: `tree /f pathname` 
- remove unempty dirctory: `Remove-Item <foldername>  -Recurse -Force`
## Linux


## Emoji 

### ✅ Status / Progress
| Emoji | Meaning                |
|-------|------------------------|
| ✅     | Success / Done         |
| ❌     | Error / Failed         |
| ⚠️     | Warning               |
| 🔄     | In Progress / Refresh  |
| 🔍     | Searching / Scanning   |
| 🔧     | Config / Setup         |
| 💾     | Saving / Backup        |
| 🛠️     | Tools / Processing     |
| ⏳     | Waiting / Loading      |

### 📂 Files & Folders
| Emoji | Meaning                |
|-------|------------------------|
| 📂     | Open folder            |
| 📁     | Closed folder          |
| 📄     | Document / File        |
| 📑     | Section / Bookmark     |
| 🗂️     | File Organizer         |
| 📝     | Writing / Notes        |

### 📶 Network & Data Transfer
| Emoji | Meaning                |
|-------|------------------------|
| 📶     | Signal / Network       |
| 📡     | Download / Comm        |
| 📲     | Upload / Mobile        |
| 🔌     | Connect / Plug         |
| 🌐     | Internet / Web         |

### 📊 Data & Analytics
| Emoji | Meaning                |
|-------|------------------------|
| 📊     | Bar Chart              |
| 📈     | Line Chart Up          |
| 📉     | Line Chart Down        |
| 🧮     | Calculation / Stats    |

### 🧪 Testing & Debugging
| Emoji | Meaning                |
|-------|------------------------|
| 🧪     | Testing / Experiment   |
| 🧬     | Data Science / DNA     |
| 🔬     | Debug / Inspection     |

### 👨‍💻 Coding & Terminal
| Emoji | Meaning                |
|-------|------------------------|
| 💻     | Laptop / Dev Work      |
| 👨‍💻    | Programmer             |
| ⌨️     | Keyboard               |
| 🖥️     | Monitor / Desktop      |
| 🧾     | Logs / Reports         |

### 🚀 Deployment & Lifecycle
| Emoji | Meaning                |
|-------|------------------------|
| 🚀     | Launch / Deploy        |
| 🛫     | Begin / Takeoff        |
| 🛬     | End / Landing          |
| 🔚     | Finish / End           |

