import timeit
import sys
from functools import lru_cache

# def recursive():
#     recursive()
#
#
# recursive()


def fib_iter(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

setup_ = "from __main__ import fib_iter"
stmt = "fib_iter(15)"

print(fib_iter(15))
print(timeit.timeit(setup=setup_, stmt=stmt, number=20000))

@lru_cache()
def fib_rec(n):
    if n <= 1:
        return n
    else:
        return (fib_rec(n - 1) + fib_rec(n - 2))


setup_ = "from __main__ import fib_rec"
stmt = "fib_rec(15)"

print(fib_rec(15))
print(timeit.timeit(setup=setup_, stmt=stmt, number=20000))