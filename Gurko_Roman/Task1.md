1. Создать локальную директорию и инициировать ее для git
$ mkdir Topic_2_GIT

$ cd Topic_2_GIT/

$ git init

2. Создать текстовый файл в директории и выполнить коммит
$ touch test.txt

$ git add .

$ git commit -m"added text file"

3. Создать удаленный репозиторий на GitHub

4. Отправить (Push) локальный репозиторий в GitHub

$ git remote add origin https://github.com/rgurko/Topic_2_GIT.git

$ git branch -M main

$ git push -u origin main

5. Создать новую ветку (назвать develop) и переключиться на нее

$ git branch develop

$ git checkout develop

6. Создать новую ветку от 'develop' и переключиться на нее

$ git checkout -b dev_test

7. Добавить первую строку в текстовый файл, выполнить коммит и отправить в репозиторий

$ nano test.txt

$ git add .

$ git commit -m"added branches and text line"

$ git push -u origin main

8. Клонировать ваш репозиторий с GitHub в отдельную директорию

$ cd ..

$ mkdir Topic_2_GIT_Clone

$ cd Topic_2_GIT_Clone

$ git clone https://github.com/rgurko/Topic_2_GIT.git

9. Создать другую ветку от ветки 'develop' и переключиться на нее, используя клонированный проект

$ git checkout develop

$ git branch -a

$ git checkout -b dev_test2

10. Добавить первую строку в текстовый файл (отличный от первой ветки), выполнить коммит и отправить в удаленный реозиторий

$ nano test.txt

$ git add .

$ git commit -m"text file is changed"

$ git push origin --all

11. Переключиться на 'develop'

$ git checkout develop

12. Объединить (merge) первую ветку и отправить (push) изменения

$ git merge dev_test -m"merging test 1"

$ git push origin --all

$ git branch -a dev_test2

13. Объединить (merge) вторую ветку и отправить (push) изменения

$ git merge dev_test2 -m"merging test 2"

$ git push origin --all

14. Разрешить конфликты, если необходимо
15. Все использованные команды записать в отдельный файл и отправить в репозиторий под именем Task1.md
