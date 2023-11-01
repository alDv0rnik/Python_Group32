"""
Даны 3  целых числа a, b и c. Найти и вывести количество отрицательных.
Для ввода чисел использовать соответствующую функцию
"""

a, b, c = int(input()), int(input()), int(input())
count = 0
if a < 0:
    count += 1
if b < 0:
    count += 1
if c < 0:
    count += 1
print(count)
