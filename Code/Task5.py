"""
Создайте собственное исключение, которое будет вызываться в случае,
если в функцию check_len() передано слово длиннее четырёх символов.
"""


class CheckLenError(Exception):
    def __init__(self, len_):
        self.len_ = len_

    def __str__(self):
        return f"Wrong length {self.len_}. Length must be less than 4"


def check_len(string_: str) -> bool:
    if len(string_) >= 4:
        raise CheckLenError(len(string_))
    return True


try:
    str_ = input()
    check_len(str_)
except CheckLenError as err:
    print(err)
