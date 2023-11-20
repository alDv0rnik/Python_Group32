"""
Написать функцию, которая принимает список целых чисел, а возвращает максимальное значение этого списка.
Вход:[-45, 2, 5, -7, -78]
Выход: 5
"""
from typing import List


def get_max(lst: List[int]) -> int:
    return max(lst)


print(get_max([-45, 2, 5, -7, -78]))


# def foo(bar=[]):
#     bar.append(1)
#     return bar

def foo(bar=None):
    if bar == None:
        bar = []
    bar.append(1)
    return bar


print(foo())
print(foo())
