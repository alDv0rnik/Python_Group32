"""
Вирус повредил систему прав доступа к файлам.
Известно, что над каждым файлом можно производить определенные действия:

запись – W;
чтение – R;
запуск – X.
На вход программе подается:

число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt

Пример вывода:
Access denied
OK
OK
OK
OK
"""

operations = {
    "read": "R",
    "write": "W",
    "execute": "X"
}
files = {}
tmp = []

n = int(input())
for i in range(n):
    data = input().split()
    files[data[0]] = data[1:]
m = int(input())
for i in range(m):
    data_ = input().split()
    operation = operations.get(data_[0])
    if operation in files.get(data_[1]):
        tmp.append("Ok")
    else:
        tmp.append("Access denied")

print(*tmp, sep="\n")
