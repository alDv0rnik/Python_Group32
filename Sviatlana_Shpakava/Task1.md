1 вариант
git clone https://github.com/Shpakava/Python_Group32.git
cd Python_Group32/
git remote add upstream https://github.com/alDv0rnik/Python_Group32.git
git remote –v
git pull
git checkout Topic_2_GIT
cd Sviatlana_Shpakava/
nano Task1.md
git status
git add .
git commit –m ‘modified Task1.md’
git push
git checkout master
git branch develop
git checkout develop
git branch develop1
git checkout develop1
nano Task1.md
git status
git add .
git commit –m ‘modified Task1.md on develop1’
git push - -set-upstream origin develop1
git checkout develop
git push - -set-upstream origin develop
git branch develop2
git checkout develop2
git push - -set-upstream origin develop2
git nano Task1.md
git status
git add .
git commit –m ‘modified Task1.md on develop2’
git checkout develop1
git merge develop2
CONFLICT
nano Task1.md
git status
git add .
git commit
git checkout Topic_2_GIT
git merge develop1
CONFLICT
nano Task1.md
git add .
git commit –m ‘conflict resolved’
git push

2 вариант
mkdir local
git init
cd local
nano File.txt
git add .
git commit –m ‘new File.txt’
git push - -set -upstream Local_Repository master
git fetch
git branch develop
git checkout develop
git branch develop1
git checkout develop1
nano File.txt
git add File.txt
git commit –m ‘new File.txt on develop1’
git push - -set -upstream Local_Repository develop1
git checkout develop
git branch develop2
git checkout develop2
nano File.txt
git add File.txt
git commit –m ‘new File.txt on develop2’
git push - -set -upstream Local_Repository develop2
git checkout develop
git push - -set -upstream Local_Repository develop
git merge develop1
git merge develop2
CONFLICT
nano File.txt
git add .
git commit –m ‘conflict resolved’
git push
