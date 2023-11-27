"""
Дано натуральное число N, вывести все натуральные числа от N до 1 (и 1 до N),
не используя циклы
"""


def get_nums(n):
    print(n)
    if n == 1:
        return n
    return get_nums(n - 1)


get_nums(5)


def get_num_1(n, current=1):
    print(current)
    if current == n:
        return n
    return get_num_1(n, current=current + 1)


get_num_1(5)