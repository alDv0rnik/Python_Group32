"""
Напишите рекурсивную функции для вычисления последовательности
n + (n – 2) + (n – 4)... (n – x =< 0),
где n – натуральное четное число.
"""


def sum_numbers(n):
    if n < 1:
        return 0
    return n + sum_numbers(n - 2)


print(sum_numbers(2))
