"""
Напишите генераторную функцию для задания 2.б
В качестве аргументов она должна принимать количество элементов и диапазон.
"""
import random


def random_generator(min, max, n):
    for _ in range(n):
        yield random.randint(min, max)


rand = random_generator(5, 20, 3)
print(next(rand))
print(next(rand))
print(next(rand))
