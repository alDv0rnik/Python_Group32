"""
Реализуйте класс CustomException, от которого создайте классы для различных видов исключений.

Реализация функции для проверки четности числа. Обработайте различные исключения для этой ошибки.
Пользовательские исключения должны быть получены из пользовательского CustomException (не из BaseException)
"""
from exceptions.custom_exceptions import WrongTypeOfArgument


def check_numbers(num: int) -> bool:
    if not isinstance(num, int):
        raise WrongTypeOfArgument
    return num % 2 == 0

print(check_numbers(4))
