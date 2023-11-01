"""
Написать программу, которой на вход подается целое трёхзначное число a.
Вывеcти количество чётных цифр в данном числе.
"""

num = input()
first = int(num[0])
second = int(num[1])
third = int(num[2])
n = 0
if first % 2 == 0:
    n += 1
if second % 2 == 0:
    n += 1
if third % 2 == 0:
    n += 1
print(n)

