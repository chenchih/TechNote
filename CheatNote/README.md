# Cheat Sheet
Record Cheat Sheet Note
## Update Record
- 2025.2.24: 
	- update git push setting
	- window shortcut	
## Git Command 

### Git push and upstream setting

#### setting git push:`upsteam` and `-u`
The point of setting upstream is to then simply use git push in the future.

- `git branch --set-upstream-to=origin/branchname`
>> - This command only establishes the upstream tracking. It tells your local branch, "This remote branch (origin/branchname) is where I should be pushing to by default."
>> - It does not push any code.

- `git push -u origin branchname`
>> - It pushes your local branch to the remote branch (origin/branchname).
>> - It sets the upstream tracking for your local main branch to origin/main
>> - Prepares your local branch and pushes the code in one command.

- `git branch -vv` : Checking Upstream Settings

#### git push 
- `git push origin main`
>> - **Bypassing Upstream**
>> - Explicitly telling Git push my current branch to origin/main, regardless of what my upstream setting is
>> - This command pushes your local branch to the remote branch (`origin/branchname`).


###  Create, Push and Pull from local to server
imagine PC1 use at office, and PC2 use at home. 

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