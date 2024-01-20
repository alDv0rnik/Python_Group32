"""
Реализуйте класс CustomException, от которого создайте классы для различных видов исключений.

Реализация функции для проверки четности числа. Обработайте различные исключения для этой ошибки.
Пользовательские исключения должны быть получены из пользовательского CustomException (не из BaseException)
"""
from exceptions.my_exceptions import *


def check_even(num: int):
    if isinstance(num, int):
        return True if num % 2 == 0 else False
    elif isinstance(num, str):
        raise CustomExceptionStringError()
    elif isinstance(num, float):
        raise CustomExceptionFloatError()


try:
    i = input("Enter your number: ")
    check_even(i)
except CustomExceptionFloatError as err:
    print(err)
except CustomExceptionStringError as err_:
    print(err_)
except ValueError as err:
    print(err)
