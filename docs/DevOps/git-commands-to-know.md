# Git commands to know

## Inspection
- ```git diff```
    - See all file changes locally. A file name can be appended to show changes for only one file.
- ```git log```
    - See all commit history. 
    - ```git log -p my_file```
        - This can be used for a file.
- ```git blame my_file```
    -  See who changed what and when in my_file.
- ```git reflog``` 
    - Show a log of changes to the local repository’s HEAD. Good for finding lost work.

## Undoing
- ```git reset```
    - It can be used on both **commits and individual files**. It is used when working locally and commits have not been merged into collaborative remote work. 
    - ```git reset --hard HEAD``` -- Discard staged and unstaged changes since the most recent commit. Specify a different commit instead of `HEAD` to discard changes since that commit. `--hard` specifies that both the staged and unstaged changes are discarded.

- ```git checkout``` 
    - It can be used on both **commits and individual files**. It is used when working locally and commits have not been merged into collaborative remote work. 
    - ```git checkout my_commit``` -- Discard unstaged changes since `my_commit`. 
        - `HEAD` is often used for `my_commit` to discard changes to your local working directory since the most recent commit.
    - ```git checkout``` is best used for local-only undo. It doesn’t mess up the commit history from a remote branch that your collaborators are depending upon. 
    - If you use ```git checkout``` with a branch instead of a commit, `HEAD` is switched to the specified branch and the working directory is updated to match. This is the more common use of the checkout command.

- ```git revert``` 
    - It is used only at the **commit** level. It is used when working collaboratively and need to neutralize a commit in the remote branch. 
    - ```git revert my_commit``` -- Undo the effects of changes in `my_commit`. 
    - It makes a new commit when it undo the changes.
    - This is safe for collaborative projects because it doesn’t overwrite history that other users’ branches might depend upon.

- ```git clean```
    - Delete untracked files in the local working directory.
    - `-n` flag is for a dry run where nothing is deleted.
    - `-f` flag is to actually remove the files.
    - `-d` flag is to remove untracked directories.

## Tidying things
- ```git commit --amend``` 
    - Add your staged changes to the most recent commit.
    - If nothing is staged, this command just allows you to edit the most recent commit message. 
    - Only use this command if the commit has not been integrated into the remote master branch.
- ```git push my_remote --tags```
    - Send all local tags to the remote repo. 
    - Good for versioning changes.
