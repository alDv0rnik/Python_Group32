"""
Напишите программу, которая получает на вход три слова и определяет,
являются ли они анаграммами друг друга.
кластер
стрелка
сталкер

>>> True
"""
from collections import Counter

str1 = "кластер"
str2 = "стрелка"
str3 = "сталкер"

counter = Counter(str1)
print(dict(counter))




# print("Ok" if set(str1) == set(str2) == set(str3) else "Not Ok")
