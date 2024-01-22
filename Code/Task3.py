"""
Сделайте строку, которая состоит из 25 случайных букв английского алфавита. Запишите ее
в файл random_string.txt

"""
import string
import random

abc = string.ascii_lowercase
result_string = ""

# 1) способ

for _ in range(25):
    result_string += abc[random.randint(0, 25)]


# 2) способ
res = list(abc[:25])
random.shuffle(res)
print("".join(res))

# 3) способ
res_str = "".join(set(abc[:25]))

# print(len(res_str))


with open("random_string.txt", "w") as file:
    file.write(result_string)

with open("random_string1.txt", "w") as file:
    file.write("".join(res))
