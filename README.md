# Python Basics
## Общие принципы выполнения заданий

Вы можете использовать PyCharm IDE для выполнения домашних задач. Однако, вы можете использовать любые другие ID, с которыми вам удобно работать. При выполнении домашнего задания важно соблюдать следующие принципы:
1. Создать вилку от текущего репозитория https://github.com/alDv0rnik/Python_Group32.git Подробную инструкцию можно найти по ссылке https://docs.github.com/en/get-started/quickstart/fork-a-repo
2. Клонировать форкнутый репозиторий на локальную машину
   ```
   git clone <link_to_your_repo>
   ```
   Важно добавить возможность отслеживать исходный репозиторий
   ```
   git remote add upstream https://github.com/alDv0rnik/Python_Group32.git
   ```
   Проверить можно командой (должно появиться 4 строки)
   ```
   git remote -v
   ```
3. Создать ветку с темой урока (важно чтобы она называлась также как в удаленном репозитории) и подтянуть актуальные изменения, если необходимо. Названия лучше давать на английском языке
   ```
   git pull --rebase <local_branch_name> origin/<remote_branch_name>
   ```
4. Создать директорию с вашим именем. Например, ```User Userovich```
5. В директории должны находиться файлы с выполненными заданиями. Например:
   ```
   Branch: Topic_1
         User_Userovich
              |___Task1.py
              |___Task2.txt
   Branch: Topic_2
         User_Userovich
              |___Task1.py
              |___Task2.py
   ```
6. Залить изменения в удаленный репозиторий в соответствующую ветку
7. Когда закончите работу, выполнить pull request в соответствующую ветку главного репозитория (от которого делалась вилка) https://github.com/alDv0rnik/Python_Group32.git
   Подробная инструкция по работе с pull request здесь: https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
   Pull request (PR) должен сопровождаться хорошим описанием. Например, 
   Название PR `Название темы - Имя Фамилия`.
   Тело PR содержит описание `Finished: Task 1.2, Task 1.3, Task 1.6`# Python_Group32