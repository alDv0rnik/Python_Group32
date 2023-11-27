import timeit

import sys
from functools import lru_cache


"""
1. Создать условие выхода из рекурсии
2. Вызов рекурентной функции
"""


def recursive():
    recursive()


recursive()


# def cut_string(s: str) -> str:
#     print(s)
#     if len(s) <= 1:
#         return s
#     return cut_string(s[:-1])
#
#
# cut_string("Hello")

@lru_cache()
def fib_iter(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


setup_rec = "from __main__ import fib_iter"
stmt_ = "fib_iter(12)"
print(fib_iter(12))
print(timeit.timeit(setup=setup_rec, stmt=stmt_, number=20000))


@lru_cache()
def fib_rec(n):
    if n <= 1:
        return n
    return (fib_rec(n - 1) + fib_rec(n - 2))


setup_rec = "from __main__ import fib_rec"
stmt_ = "fib_rec(12)"
print(fib_rec(12))
print(timeit.timeit(setup=setup_rec, stmt=stmt_, number=20000))


print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())