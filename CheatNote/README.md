# Cheat Sheet
Record Cheat Sheet Note
## Update Record
- 2025.2.24: 
	- update git push setting
	- window shortcut	
## Git Command 

###  Adding Branch 

**Description: PC1 main and tmp branch, PC2 main branch**
```
#PC1 create new branch: 
git checkout -b tmp #create and change new branch in local side
git add
git commit 
#git push
git push -u origin <branch name>

#PC2: want to pull the new branch to local side:
git checkout -b tmp #create new branch and in local side

git fetch origin
git pull origin tmp
```

**ignore local git:** `git stash` and pull latest code

### Git push and upstream setting

#### setting git push:  `upsteam` and `-u`
The point of setting upstream is to then simply use git push in the future.

- `git branch --set-upstream-to=origin/branchname`
> - This command only establishes the upstream tracking. It tells your local branch, "This remote branch (origin/branchname) is where I should be pushing to by default."
> - It does not push any code.

- `git push -u origin branchname`
> - It pushes your local branch to the remote branch (origin/branchname).
> - It sets the upstream tracking for your local main branch to origin/main
> - Prepares your local branch and pushes the code in one command.

- `git branch -vv` : Checking Upstream Settings

#### git push 
- `git push origin main`
> - Bypassing Upstream
> - you're explicitly telling Git: "Push my current branch to origin/main, regardless of what my upstream setting is
> - This command pushes your local branch to the remote branch (`origin/branchname`).

## PYTHON

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