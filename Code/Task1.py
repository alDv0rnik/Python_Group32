"""
Напишите декоратор @timer к функции нахождения факториала числа и выведите время выполнения кода
"""
from decorators import timer, slowdown
import time


@timer
@slowdown(0.5)
def get_factorial(num):
    if num == 1:
        return num
    return num * get_factorial(num - 1)


get_factorial(6)