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
The point of setting upstream is to then simply use git push in the future.

- `git branch --set-upstream-to=origin/branchname`
	- This command only establishes the upstream tracking. It tells your local branch, "This remote branch (origin/branchname) is where I should be pushing to by default."
	- It does not push any code.

- `git push -u origin branchname`
	- It pushes your local branch to the remote branch (origin/branchname).
	- It sets the upstream tracking for your local main branch to origin/main
	- Prepares your local branch and pushes the code in one command.

- `git branch -vv` : Checking Upstream Settings

#### git push 
- `git push origin main`
	- **Bypassing Upstream**
	- Explicitly telling Git push my current branch to origin/main, regardless of what my upstream setting is
	- This command pushes your local branch to the remote branch (`origin/branchname`).


###  Create, Push and Pull from local to server
imagine PC1 use at office, and PC2 use at home. 

- create branch:`git checkout <branch_name>`
- remove local branch: `git branch [-D|-d] <branch_name>`
	- `-d`: checks if the branch has been fully merged into its upstream branch. If it has, it deletes the branch. If not, it will return an error.
	- `-D`: If you want to force deletion (even if it's not fully merged)
- remove remote branch: `git push origin --delete <branch_name>` or `git push origin :<branch_name>`

#### Case1: Push remote branch with same and different branch name

##### 1.1 PC1 push same branch name as local and remote
This example will show using same branch name on both local and remote. 

> - Create local `tmp` branch and push to remote branch `tmp` 
Local branch and remote branch use the same name
```
git checkout -b tmp #create and change new branch in local side
git add .
git commit -m <message to commit> 

#Pushes your current local branch to a remote branch with the same name
git push -u origin <remote branch name, ex:tmp>

```
##### 1.2 PC1 push local main branch to remote with different name
Pushes the local main branch to the remote tmp branch. If tmp doesn't exist on the remote, it will be created.
```
#better way of using git pul:
git pull #git fetch+git merge
git pull --rebase #use this instead of git pull
#these are other option:
git pull --ff only #only fetch new commit 
git pull -- ff

```

> - Push local `main` branch to remote branch `tmp`(or different remote branch name)
Local branch and remote branch use different name
```
#main branch 
git add .
git commit -m <message to commit> 
#Pushes your local main branch to a remote branch named tmp branch
git push origin main:tmp #Does not set upstream tracking.
```

#### Case2 PC2 pull remote origin/tmp to local tmp branch(auto create it)
This command creates a new local branch tmp that tracks the remote `origin/tmp branch` and switches to it. 
This is PC2 which don't have `tmp` branch in local side, and want to download remote `origin/tmp` data to local side. In PC2 just `case1-1` or `case1-2` create a remote branch `tmp`, if you want the branch to download local branch, just this method. 

```
git fetch --all #will update remote branch list
git checkout -b tmp origin/tmp
git commit -m "commit msg"
git push -u origin tmp
```

you can use the `remote branch -r` to see your updated remote list. 


#### Case3: PC1 pull origin/tmp to local main without create any branch
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
- `git stash`: is a local operation. It does not interact with remote repositories. It is a temporary holding area for your uncommitted changes.
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

I am editing test.py. Then, there are some new updates on the remote. I need to save my uncommitted changes and perform a git pull to update my local repository with the latest changes from the remote. In this case, I will use git stash to save my uncommitted changes to a temporary location (the stash).

Now, I will use git pull to fetch and merge the latest changes from the remote into my current local branch. After the git pull is complete, I will use git stash pop to reapply the changes I made to test.py before the pull.


### Visualize your Git branch graph 
- `git log --graph --oneline --decorate --all`
- `gitk --all` : (GUI)


## PYTHON

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

## 📌 How to Use
```python
print("✅ Process completed.")
print("📂 Opening file...")
print("📊 Generating report...")
print("🛠️ Running diagnostics...")
```