
Dmitriy@LAPTOP-QU8O787F MINGW64 ~ (master)
$ mkdir repo_git

Dmitriy@LAPTOP-QU8O787F MINGW64 ~ (master)
$ git clone https://github.com/shleg87/repo_git.git
Cloning into 'repo_git'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~ (master)
$ cd repo_git

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ ls -l
total 1
-rw-r--r-- 1 Dmitriy 197121 22 Oct 27 10:49 README.md

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git remove
git: 'remove' is not a git command. See 'git --help'.

The most similar command is
        remote

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git remote
origin

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ vi README.md

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git add .

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git commit -m "New file"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Dmitriy@LAPTOP-QU8O787F.(none)')

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$  git config --local user.email "shleg87@gmail.com git config --local user.email "shleg87@gmail.com""

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git config --local user.name "shleg87"

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git config --local -l
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
remote.origin.url=https://github.com/shleg87/repo_git.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
user.email=shleg87@gmail.com git config --local user.email shleg87@gmail.com
user.name=shleg87

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git push -u origin main
Everything up-to-date
branch 'main' set up to track 'origin/main'.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git commit -u "New commit"
error: pathspec 'New commit' did not match any file(s) known to git

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git commit -m "New file"
[main cdf2ba6] New file
 1 file changed, 1 insertion(+), 1 deletion(-)

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 284 bytes | 284.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/shleg87/repo_git.git
   c4bad8b..cdf2ba6  main -> main

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git log --oneline
cdf2ba6 (HEAD -> main, origin/main, origin/HEAD) New file
c4bad8b Initial commit

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ hit branch
bash: hit: command not found

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git branch
* main

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git checkout -b "developer"
Switched to a new branch 'developer'

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git branch "developer"
fatal: a branch named 'developer' already exists

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git status
On branch developer
nothing to commit, working tree clean

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git checkout

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git branch
* developer
  main

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git checkout -b "developer1"
Switched to a new branch 'developer1'

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git branch
  developer
* developer1
  main

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ nano

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git status
On branch developer1
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        y

nothing added to commit but untracked files present (use "git add" to track)

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git add .
warning: in the working copy of 'y', LF will be replaced by CRLF the next time Git touches it

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git status
On branch developer1
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   y


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git commit -m "y file"
[developer1 be96c1f] y file
 1 file changed, 1 insertion(+)
 create mode 100644 y

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ nano

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git status
On branch developer1
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git file

nothing added to commit but untracked files present (use "git add" to track)

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git add .
warning: in the working copy of 'git file', LF will be replaced by CRLF the next time Git touches it

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git status
On branch developer1
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   git file


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git commit -m "File git"
[developer1 810e0f6] File git
 1 file changed, 1 insertion(+)
 create mode 100644 git file

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git commit
On branch developer1
nothing to commit, working tree clean

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git clone repo_git
fatal: repository 'repo_git' does not exist

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git clone my-new-project
fatal: repository 'my-new-project' does not exist

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ ls -l
total 3
-rw-r--r-- 1 Dmitriy 197121 29 Oct 27 10:52  README.md
-rw-r--r-- 1 Dmitriy 197121 10 Oct 27 11:52 'git file'
-rw-r--r-- 1 Dmitriy 197121 15 Oct 27 11:46  y

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git clone https://github.com/shleg87/my-new-project.git
Cloning into 'my-new-project'...
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 13 (delta 0), reused 6 (delta 0), pack-reused 0
Receiving objects: 100% (13/13), done.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git status
On branch developer1
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        my-new-project/

nothing added to commit but untracked files present (use "git add" to track)

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git add .
warning: adding embedded git repository: my-new-project
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint:   git submodule add <url> my-new-project
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint:   git rm --cached my-new-project
hint:
hint: See "git help submodule" for more information.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git status
On branch developer1
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   my-new-project


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ ls -l
total 3
-rw-r--r-- 1 Dmitriy 197121 29 Oct 27 10:52  README.md
-rw-r--r-- 1 Dmitriy 197121 10 Oct 27 11:52 'git file'
drwxr-xr-x 1 Dmitriy 197121  0 Oct 27 11:59  my-new-project/
-rw-r--r-- 1 Dmitriy 197121 15 Oct 27 11:46  y

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git checkout developer
Switched to branch 'developer'
A       my-new-project

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git checkout -b "developer2"
Switched to a new branch 'developer2'

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ nano

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git status
On branch developer2
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   my-new-project

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        second


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git add .
warning: in the working copy of 'second', LF will be replaced by CRLF the next time Git touches it

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git status
On branch developer2
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   my-new-project
        new file:   second


Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git commit -m "New file2"
[developer2 8c5639e] New file2
 2 files changed, 2 insertions(+)
 create mode 160000 my-new-project
 create mode 100644 second

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git branch
  developer
  developer1
* developer2
  main

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git fetch

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer2)
$ git checkout "developer"
warning: unable to rmdir 'my-new-project': Directory not empty
Switched to branch 'developer'

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ ls -l
total 1
-rw-r--r-- 1 Dmitriy 197121 29 Oct 27 10:52 README.md
drwxr-xr-x 1 Dmitriy 197121  0 Oct 27 11:59 my-new-project/

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git merge "repo_git"
merge: repo_git - not something we can merge

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git merge "developer1"
Updating cdf2ba6..810e0f6
Fast-forward
 git file | 1 +
 y        | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 git file
 create mode 100644 y

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git push origin main
Everything up-to-date

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ ls -l
total 3
-rw-r--r-- 1 Dmitriy 197121 29 Oct 27 10:52  README.md
-rw-r--r-- 1 Dmitriy 197121 11 Oct 27 12:12 'git file'
drwxr-xr-x 1 Dmitriy 197121  0 Oct 27 11:59  my-new-project/
-rw-r--r-- 1 Dmitriy 197121 16 Oct 27 12:12  y

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer)
$ git checkout "main"
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        my-new-project/

nothing added to commit but untracked files present (use "git add" to track)

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git marge "developer"
git: 'marge' is not a git command. See 'git --help'.

The most similar command is
        merge

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git checkout "developer1"
Switched to branch 'developer1'

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git merge "developer"
Already up to date.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (developer1)
$ git checkout "main"
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git merge "developer1"
Updating cdf2ba6..810e0f6
Fast-forward
 git file | 1 +
 y        | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 git file
 create mode 100644 y

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$ git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 548 bytes | 548.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/shleg87/repo_git.git
   cdf2ba6..810e0f6  main -> main

Dmitriy@LAPTOP-QU8O787F MINGW64 ~/repo_git (main)
$

