"""
Напишите функцию для вычисления факториала числа рекурссивно.
Решите задачу двумя способами – итеративным и рекурсивным.
"""


def get_factorial(n):
    if n == 1:
        return n
    return n * get_factorial(n - 1)


print(get_factorial(1))


