"""
Сделайте строку, которая состоит из 25 случайных букв английского алфавита. Запишите ее
в файл random_string.

"""
import string
import random

abc = string.ascii_lowercase
random_letters = ""
n = 25

while len(random_letters) < n:
    letter = abc[random.randint(0, len(abc) - 1)]
    random_letters += letter

with open("random_string.txt", 'w') as file:
    file.write(random_letters)



