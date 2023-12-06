"""
написать декоратор-дебагер для функции нахождения факториала
"""
from decorators import debug_this, timer


@debug_this
def get_factorial(num):
    if num == 1:
        return num
    return num * get_factorial(num - 1)


# print(get_factorial(5))


@debug_this
def get_sum(a, b, c, d):
    """
    This is simple function
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    return a + b + c + d


print(get_sum(4, 5, 6, 7))
print(get_sum.__name__)
print(get_sum.__doc__)