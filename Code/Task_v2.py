"""
Написать функцию, которая проверяет сложность пароля.
Пароль считается валидным, если содержит не менее 8 символов, как минимум 1 цифру, одну букву в uppercase
и 1 специальный символ

Функция должна вернуть True, если пароль валидный и False, если наоборот
"""


def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    else:
        if not password.islower() and not password.isupper() and not password.isdigit():
            for elem in password:
                if elem in "!@:,.<>?{}[]()$#":
                    return True
        return False


print(is_valid_password("(((((((((("))