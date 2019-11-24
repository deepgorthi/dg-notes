# Git Process

## Initializing a repo and committing files

To store a directory under version control you need to create a repository. With Git you initialise a repository in the top-level directory for a project. As this is a new project, a new repository needs to be created. Use the ```git init``` command to create a repository.

When a directory is part of a repository it is called a Working Directory. A working directory contains the latest downloaded version from the repository together with any changes that have yet to be committed. You can view which files have changed between your working directory and what's been previously committed to the repository using the command ```git status```.

To save, or commit, files into your Git repository you first need to add them to the staging area. 
Git has three areas, 
- a working directory
- a staging area
- the repository itself.

Use the command ```git add <file|directory>``` to add a file or folder to the staging area.

Once a file has been added to the staging area it needs to be committed to the repository. Use ```git commit -m "<commit message>"``` to commit the staged file. Each commit is assigned a SHA-1 hash which enables you to refer back to the commit in other commands.

The ```.gitignore``` should be committed to the repository to ensure the rules apply across different machines.

```bash
Pradeeps-MBP:learning-git pradeepgorthi$ git init
Initialized empty Git repository in /Users/pradeepgorthi/Documents/github-repos/learning-git/.git/
Pradeeps-MBP:learning-git pradeepgorthi$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	Notes.md

nothing added to commit but untracked files present (use "git add" to track)
Pradeeps-MBP:learning-git pradeepgorthi$ git add Notes.md
Pradeeps-MBP:learning-git pradeepgorthi$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   Notes.md

Pradeeps-MBP:learning-git pradeepgorthi$ git commit -m "learning git initial commit with commit notes"
[master (root-commit) 5e7bc28] learning git initial commit with commit notes
 1 file changed, 28 insertions(+)
 create mode 100644 Notes.md
Pradeeps-MBP:learning-git pradeepgorthi$ git status
On branch master
nothing to commit, working tree clean
```

---
## Committing Changes

As discussed in the previous scenario ```git status``` allows us to view the changes in the working directory and staging area compared to the repository.

The command ```git diff``` enables you to compare changes in the working directory against a previously committed version. By default the command compares the working directory and the HEAD commit.

If you wish to compare against an older version then provide the commit hash as a parameter, for example ```git diff <commit>```. Comparing against commits will output the changes for all of the files modified. If you want to compare the changes to a single file then provide the name as an argument such as ```git diff committed.js```

```bash
  > git diff
diff --git a/committed.js b/committed.js
index 12e7e7c..fc77969 100644
--- a/committed.js
+++ b/committed.js
@@ -1 +1 @@
-console.log("Committed File")
+console.log("Demostrating changing a committed file")
```

As in the previous scenario in order to commit a change it must first be staged using ```git add``` command.

If you rename or delete files then you need to specify these files in the add command for them to be tracked. Alternatives you can use ```git mv``` and ```git rm``` for git to perform the action and include update the staging area.

Once the changes are in the staging area they will not show in the output from ```git diff```. By default, it will only compare the working directory and not the staging area.

To compare the changes in the staging area against the previous commit, provide the staged parameter ```git diff --staged``` to ensure that you have correctly staged all your changes.

```bash
 > git diff --staged
diff --git a/committed.js b/committed.js
index 12e7e7c..fc77969 100644
--- a/committed.js
+++ b/committed.js
@@ -1 +1 @@
-console.log("Committed File")
+console.log("Demostrating changing a committed file")
diff --git a/untracked.js b/untracked.js
new file mode 100644
index 0000000..264a5be
--- /dev/null
+++ b/untracked.js
@@ -0,0 +1 @@
+console.log("Untracked File")
```

The command ```git log``` allows you to view the history of the repository and the commit log.

```bash
  > git log
commit 8e406ea6214f7c89cd732ed8ee43b4e4ee121e24
Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
Date:   Wed Sep 18 15:44:53 2019 +0000

    Changed the output message in committed.js

commit 44a3b80bfcdf8a18688cad2149ca8494f7da91a1
Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
Date:   Wed Sep 18 15:19:35 2019 +0000

    Initial Commit
```

The format of the log output is very flexible.
```bash
  > git log --pretty=format:"%h %an %ar - %s"
8e406ea Scrapbook Git Tutorial 2 minutes ago - Changed the output message in committed.js
44a3b80 Scrapbook Git Tutorial 27 minutes ago - Initial Commit
```

While git log tells you the commit author and message, to view the changes made in the commit you need to use the the command ```git show```. Use ```git show <commit-hash>``` to view older changes.

```bash
> git show
commit 8e406ea6214f7c89cd732ed8ee43b4e4ee121e24
Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
Date:   Wed Sep 18 15:44:53 2019 +0000

    Changed the output message in committed.js

diff --git a/committed.js b/committed.js
index 12e7e7c..fc77969 100644
--- a/committed.js
+++ b/committed.js
@@ -1 +1 @@
-console.log("Committed File")
+console.log("Demostrating changing a committed file")
diff --git a/untracked.js b/untracked.js
new file mode 100644
index 0000000..264a5be
--- /dev/null
+++ b/untracked.js
@@ -0,0 +1 @@
+console.log("Untracked File")

```

Here is an interesting image to refer to when using git.

![image](gitimage.jpg)

---
## Working Remotely

Remote repositories allow you to share changes from or to your repository. Remote locations are generally a build server, a team members machine or a centralised store such as Github.com.

Remotes are added using the ```git remote``` command with a friendly name and the remote location, typically a HTTPS URL or a SSH connection.

```bash
  > git remote add test-name /s/remote-project/1
```

```bash
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags|--no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete |<branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand
```

If you use ```git clone```, then the location being cloned will be automatically added as a remote with the name origin.

```bash
Pradeeps-MBP:learning-git pradeepgorthi$ git remote add origin https://github.com/deepgorthi/learning-git.git
```

When ready to share the commits, you need to push them to a remote repository via ```git push``` and it is followed by two parameters. The first parameter is the friendly name of the remote repository we defined in the first step. The second parameter is the name of the branch. By default all git repositories have a master branch where the code is worked on.

```bash
Pradeeps-MBP:learning-git pradeepgorthi$ git push -u origin master
Username for 'https://github.com': deepgorthi
Password for 'https://deepgorthi@github.com':
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 1.62 KiB | 1.62 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/deepgorthi/learning-git.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

A typical Git workflow would be to perform multiple small commits as you complete a task and push to a remote at relevant points, such as when the task is complete, to ensure synchronisation of the code within the team.

```git pull``` allows you to sync changes from a remote repository into your local version.

Use the command ```git log --grep="#1234"``` to find all the commits containing `#1234`

The command ```git pull``` is a combination of two different commands, 
> `git pull` =>  `git fetch` + `git merge` 

Fetch downloads the changes from the remote repository into a separate branch named `remotes/<remote-name>/<remote-branch-name>`. The branch can be accessed using `git checkout`. Using `git fetch` is a great way to review the changes without affecting your current branch. The naming format of branches is flexible enough that you can have multiple remotes and branches with the same name and easily switch between them.

```bash
    > git merge remotes/<remote-name>/<remote-branch-name> master
```

You can view a list of all the remote branches using the command 
```
    > git branch -r
```

---
## Undoing Changes

The command ```git checkout``` will replace everything in the working directory to the last committed version. If you want to replace all files then use a dot (.) to indicate the current directory, otherwise list the directories/files separated by spaces.

If you're in the middle of a commit and have added files to the staging area but then changed your mind then you'll need to use the ```git reset``` command. It will move files back from the staging area to the working directory. If you want to reset all files then use a "." to indicate current directory, otherwise list the files separated by spaces.

```bash
$ git add Notes.md
$ git add gitimage.jpg
$ git reset Notes.md
    Unstaged changes after reset:
    M	Notes.md
$ git commit -m "Adding git image"
    [master 8eba1eb] Adding git image
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 gitimage.jpg
$ git push origin master
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 25.23 KiB | 8.41 MiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/deepgorthi/learning-git.git
    a0d745f..8eba1eb  master -> master
```

> `git reset --hard` => `git reset` + `git checkout`

The result of `git reset --hard` will be files removed from staging area and the working directory is taken back to the state of the last commit.

Using HEAD will clear the state back to the last commit and using ```git reset --hard <commit-hash>``` allows you to go back to any commit state. 
`HEAD` is an alias for the last commit-hash of the branch.

If you have already committed files but realized you made a mistake then the command ```git revert``` allows you to undo the commits. The command will create a new commit which has the inverse affect of the commit being reverted.

If you haven't pushed your changes then ```git reset HEAD~1``` has the same affect and will remove the last commit.

To revert multiple commits at once we use the character `~` to mean minus. For example, `HEAD~2` is two commits from the head. This can be combined with the characters `...` to say between two commits.

Use the command ```git revert HEAD...HEAD~2``` to revert the commits between HEAD and HEAD~2.

The command ```git log --oneline``` for a quick overview of the commit history.

---
## Fixing Merge Conflicts

The `git fetch` command downloads changes into a separate branch which can be checked out and merge. During a merge, Git will attempt to automatically combine the commits. When no conflicts exist then the merge will be 'fast-forwarded' and you won't have to do anything. If a conflict does exist, then you will retrieve an error and the repository will be in a merging state.

```bash
  > git fetch

  > git merge origin/master
Auto-merging staging.txt
CONFLICT (add/add): Merge conflict in staging.txt
Automatic merge failed; fix conflicts and then commit the result.
```

When a conflict occurs the changes from both the local and remote will appear in the same file in the unix diff format. To read the format, the local changes will appear at the top between `<<<<<<< HEAD` and `=======` with the remote changes being underneath between `=======` and `>>>>>>> remotes/origin/master`.

```
<<<<<<< HEAD
Fixing Error, Let's Hope No-One Else Does
=======
Fixing Previous Error
>>>>>>> origin/master
```

The simplest way to fix a conflict is to pick either the local or remote version using `git checkout --ours staging.txt` or `git checkout --theirs staging.txt`. If you need to have more control then you can manually edit the file(s) like normal.

```bash
  > git checkout --theirs staging.txt

  > git add staging.txt

  > git commit
[master 51ae805] Merge remote-tracking branch 'origin/master'
```

If you want to revert in the middle of a merge and try again then use the command `git reset --hard HEAD;` to go back to your previous state.

Use `git commit --no-edit` when you wish to use the default commit message.

To simulate a **non-fast forward merge** the following has occurred.

1) Developer A pulls the latest changes from Developer B.
2) Developer B commits changes to their local repository.
3) Developer A commits non-conflicting changes to their local repository.
4) Developer A pulls the latest changes from Developer B.

In this scenario Git is unable to fast-forward the changes from Developer B because Developer A has made a number of changes.

When this happens, Git will attempt to auto-merge the changes. If no conflicts exist then the merge will be completed and a new commit will be created to indicate the merge happening at that point in time.

The default commit message for merges is "Merge branch '' of ". These commits can be useful to indicate synchronization points between repositories but also produce a noisy commit log.

```bash
  > git pull --no-edit origin master
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (4/4), done.
From /s/remote-project/1
 * branch            master     -> FETCH_HEAD
   418fe6e..095b88a  master     -> origin/master
Merge made by the 'recursive' strategy.
 new-file-6.txt  | 1 +
 new-file-6a.txt | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 new-file-6.txt
 create mode 100644 new-file-6a.txt
```

**Git Rebase**

The merge commit messages can be useful to indicate synchronization points but they can also produce a lot of noise. For example, if you're working against local branches and haven't pushed then this additional information is meaningless, and confusing, to other developers looking at the repository.

To solve this you can use git rebase instead of git merge. A rebase will unwind the changes you've made and replay the changes in the branch, applying your changes as if they happened all on the same branch. The result is a clean history and graph for the merge.

> From [git-scm](https://git-scm.com/book/en/v2/Git-Branching-Rebasing#The-Perils-of-Rebasing):
> - The easiest way to integrate the branches, as we’ve already covered, is the merge command. It performs a three-way merge between the two latest branch snapshots (C3 and C4) and the most recent common ancestor of the two (C2), creating a new snapshot (and commit).
> - However, there is another way: you can take the patch of the change that was introduced in C4 and reapply it on top of C3. In Git, this is called rebasing. With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.

*Important:* As rebase will replay the changes instead of merging, each commit will have a new hash id. If you, or other developers, have pushed/pulled the repository then changing the history can git to lose commits. As such you shouldn't rebase commits that have been made public, for example pushing commits then rebasing in older commits from a different branch. The result will be previously public commits having different hash ids. More details can be found at [The Perils of Rebasing](https://git-scm.com/book/ch3-6.html#The-Perils-of-Rebasing).

This approach also applies when working with remote branches and can be applied when issuing a pull request using: ```git pull --rebase```

```bash
  > git pull --rebase
There is no tracking information for the current branch.
Please specify which branch you want to rebase against.
See git-pull(1) for details

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> feature/10
```
This will act as if you had done a pull request before each of your commits.

> In general, the way to get the best of both worlds is to rebase local changes you’ve made but haven’t shared yet before you push them in order to clean up your story, but never rebase anything you’ve pushed somewhere.

---
## Git Branches

A branch allows you to work in a brand new working directory efficiently. The result is that a single Git repository can have multiple different versions of the code-base, each of which can be swapped between without changing directories.

The default branch in Git is called master. When you switch a branch, Git changes the contents of the working directory. This means you don't need to change any configurations or settings to reflect different branches or locations.

Branches are created based on another branch, generally master. The command ```git branch <new branch name> <starting branch>``` takes an existing branch and creates a separate branch to work in. At this point, both branches are identical. To switch to a branch you use the ```git checkout <new branch name>``` command.

The above two commands can be combined into a single command by doing ```git checkout -b <new branch name>``` which will create and checkout the newly created branch and the starting branch defaults to `HEAD`.
```bash
> git branch new_branch master

> git checkout new_branch
    Switched to branch 'new_branch'
```

To list all the branches, use the command ```git branch```.

The additional argument -a will include remote branches while including -v will include the HEAD commit message for the branch.

```bash
> git branch -va
    master       75fa002 First Commit on master
    new_branch   75fa002 First Commit on master
    * new_branch_b 1296799 Commit on branch
```

A commit has been made to the new branch. To merge this into master, you would first need to checkout the target branch, in this case master, ```git checkout master``` and then use ```git merge <branch-name>``` command to merge in the commits from a branch.

```bash
> git status
    On branch new_branch
    nothing to commit, working directory clean

> touch test_file

> git add test_file

> git status
    On branch new_branch
    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

            new file:   test_file

> git commit -m "Adding test file to new_branch"
    [new_branch 0fceb73] Adding test file to new_branch
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test_file

> git checkout master
    Switched to branch 'master'

> git merge new_branch
    Updating 75fa002..0fceb73
    Fast-forward
    test_file | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test_file
```
To push a branch to a remote, use ```git push <remote_name> <branch_name>```
```bash
> git push origin new_branch
    Counting objects: 6, done.
    Delta compression using up to 12 threads.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (6/6), 524 bytes | 0 bytes/s, done.
    Total 6 (delta 0), reused 0 (delta 0)
    To /s/remote-project/1
    * [new branch]      new_branch -> new_branch
```

Cleaning up branches is important to remove the amount of noise and confusion. To delete a branch, you need to provide the argument -d like ```git branch -d <branch_name>```
```bash
> git branch -d new_branch
    Deleted branch new_branch (was 0fceb73).
```

---
## Finding Bugs

- ```git diff```
	- This command is the simplest to compare what's changed between commits. It will output the differences between the two commits.

```bash
> git diff HEAD~2 HEAD
	diff --git a/list.html b/list.html
	index 96e99d0..9f53aec 100644
	--- a/list.html
	+++ b/list.html
	@@ -2,4 +2,6 @@
	 <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li>
	 <li>Aliquam tincidunt mauris eu risus.</li>
	 <li>Vestibulum auctor dapibus neque.</li>
	+<li>Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a.</li>
	+<li>Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat.</li>
	 </ul>
```

- ```git log```
	- While git log helps you see the commit messages but by default it does not output what actually changed.
- ```git log --oneline```
	- To see the overview of the commits in a short view, use this command.
```bash
  > git log --oneline
	43a9071 Final Item
	49f29f0 New Item
	3c2ef9c Initial commit of the list
```

- ```git log -p```
	- To output the commit information with the differences of what changed you need to include the -p prompt
```bash
 > git log -p
	commit 43a9071cd9f4e4e17dbd1f7ee50020373a04dd6f
	Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
	Date:   Fri Sep 20 17:34:55 2019 +0000

	    Final Item

	diff --git a/list.html b/list.html
	index def310d..9f53aec 100644
	--- a/list.html
	+++ b/list.html
	@@ -3,4 +3,5 @@
	 <li>Aliquam tincidunt mauris eu risus.</li>
	 <li>Vestibulum auctor dapibus neque.</li>
	 <li>Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a.</li>
	+<li>Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat.</li>
	 </ul>

	commit 49f29f018078ec090b466edea6d57ba980e06bd3
	Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
	Date:   Fri Sep 20 17:34:55 2019 +0000

	    New Item

	diff --git a/list.html b/list.html
	index 96e99d0..def310d 100644
	--- a/list.html
	+++ b/list.html
	@@ -2,4 +2,5 @@
	 <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li>
	 <li>Aliquam tincidunt mauris eu risus.</li>
	 <li>Vestibulum auctor dapibus neque.</li>
	+<li>Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a.</li>
	 </ul>

	commit 3c2ef9c7048a9e98af1679e2b7349cbd53ec17c9
	Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
	Date:   Fri Sep 20 17:34:55 2019 +0000

	    Initial commit of the list

	diff --git a/list.html b/list.html
	new file mode 100644
	index 0000000..96e99d0
	--- /dev/null
	+++ b/list.html
	@@ -0,0 +1,5 @@
	+<ul>
	+<li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li>
	+<li>Aliquam tincidunt mauris eu risus.</li>
	+<li>Vestibulum auctor dapibus neque.</li>
	+</ul>
```

- ```git log -p -n 2```
	- This will output the entire history. You can filter it with a number of different options. The -n <number> specifies a limit of commits to display from the HEAD. Using '2' displays HEAD and HEAD~1.

```bash
  > git log -p -n 2
	commit 43a9071cd9f4e4e17dbd1f7ee50020373a04dd6f
	Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
	Date:   Fri Sep 20 17:34:55 2019 +0000

	    Final Item

	diff --git a/list.html b/list.html
	index def310d..9f53aec 100644
	--- a/list.html
	+++ b/list.html
	@@ -3,4 +3,5 @@
	 <li>Aliquam tincidunt mauris eu risus.</li>
	 <li>Vestibulum auctor dapibus neque.</li>
	 <li>Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a.</li>
	+<li>Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat.</li>
	 </ul>

	commit 49f29f018078ec090b466edea6d57ba980e06bd3
	Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
	Date:   Fri Sep 20 17:34:55 2019 +0000

	    New Item

	diff --git a/list.html b/list.html
	index 96e99d0..def310d 100644
	--- a/list.html
	+++ b/list.html
	@@ -2,4 +2,5 @@
	 <li>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</li>
	 <li>Aliquam tincidunt mauris eu risus.</li>
	 <li>Vestibulum auctor dapibus neque.</li>
	+<li>Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a.</li>
	 </ul>
```

- ```git log --grep="Initial"```
	- This will output all the commits which include the word "Initial" in their commit message. This is useful if you tag commits with bug-tracking numbers.

```bash
  > git log --grep="Initial"
	commit 3c2ef9c7048a9e98af1679e2b7349cbd53ec17c9
	Author: Scrapbook Git Tutorial <git-tutorial@joinscrapbook.com>
	Date:   Fri Sep 20 17:34:55 2019 +0000

	    Initial commit of the list
```

- ```git bisect```
	- This command allows you to do a binary search of the repository looking for which commit introduced the problem and the regression. Git bisect takes a number of steps, execute the steps in order to see the results.
	- **Steps**
		- To enter into bisect mode you use the command ```git bisect start```.
		- Once in bisect mode, define your current checkout as bad using ```git bisect bad```. This indicates that it contains the problem you are searching to see when it was introduced.
		- We have defined where a bad commit happened. Now we need to define when the last known good commit was using ```git bisect good HEAD~5```. In this case it was five commits ago.
		- The above step will checkout the commit in-between bad and good commits. You can then check the commit, run tests etc to see if the bug exists. In this example, you can check the contents using ```cat list.html``
		- This commit looks good as everything has correct HTML tags. We tell Git we're happy using ```git bisect good```. This will automatically check out the commit in the middle of the last known good commit, as defined in step 5 and our bad commit.
		- As we did before, we need to check to see if the commit is good or bad using ```cat list.html```
		- This commit has missing HTML tags. Using ```git bisect bad``` will end the search and output the the related commit id.
	- The result is that instead of searching five commits, we only searched two. On a much larger timescale, `bisect` can save you signifant time.

- ```git blame```
	- It can be useful to know who worked on a certain section of the file to help with improvements in future.
	- This command shows the revision and author who last modified each line of a file.
	- If we know the lines which we're concerned with then we can use the -L parameter to provide a range of lines to output.

---
## Being picky with Git

**Cherry Picking**

In this scenario, we only care about changes to one of the files but if we merged the branch, then we'd merge all five commits and the unwanted changes. To merge individual commits, we use ```git cherry-pick <hash-id|ref>``` command. This behaves in a similar way to *merge*, if no conflicts exist then the commit will be automatically merged. 

```new_branch~3``` refers to the second-to-last commit in the branch.

```bash
  > git log --pretty=oneline --reverse new_branch
	f3a03a060cd76c4ebd68ba2a35ad9685f041a9b6 Readme File
	2be62bb15c92ad4dfc57b62592df09907afc2c5a Initial commit, no items
	ac4d5aec7ee23de2b6b6756a598dbd5f59f65ac5 Initial list
	0e2dc8c0428a3fd5e42af547a97c5eb9828b3c4b Creating Second List
	4b4bcb18289c3adf476a97c328caaacfc0f4a9a8 Adding final items to the list

  > git cherry-pick 2be62bb15c92ad4dfc57b62592df09907afc2c5a
	[master 902442e] Initial commit, no items
	 1 file changed, 2 insertions(+)
	 create mode 100644 list.html

  > git cherry-pick ac4d5aec7ee23de2b6b6756a598dbd5f59f65ac5
	[master 903c134] Initial list
	 1 file changed, 3 insertions(+)

  > git cherry-pick 4b4bcb18289c3adf476a97c328caaacfc0f4a9a8
	[master e91edc3] Adding final items to the list
	 1 file changed, 1 insertion(+)
```

Conflicts can be solved in the same way as with merging a branch - either manually fixing the files or selecting theirs or ours via `git checkout`. You can stop and revert the pick using ```git cherry-pick --abort```

Once the conflicts have been resolved, you can continue with the cherry pick using the command ```git cherry-pick --continue```

---

## Re-writing History in Git

Re-writing the repositories history is done using ```git rebase -interactive```. This has a total of 6 commands that can be used.

```bash
> git rebase --interactive --root

# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
```

This will open up a file that can be edited in vim. If we want to correct a type in the commit message, we can change `pick` to `reword` and that will result in a new vim file opening. Now, we can change the commit message typo and then save it.

```bash
  > git rebase --interactive --root
	[detached HEAD 9eebea9] Initial commit of the list
	 1 file changed, 5 insertions(+)
	 create mode 100644 list.html
	Successfully rebased and updated refs/heads/master
```

```git commit --amend``` can be used to reword the last commit message. 

If we want to re-order our last two commits, that can be done using HEAD~2 that allows us to modify them. ```git rebase --interactive HEAD~2``` -> Using Vim, simply reorder the lines, save & quit, and the commits will match the order.

---
