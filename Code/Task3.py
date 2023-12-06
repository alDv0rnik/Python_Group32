"""
Создайте эмулятор предоставления доступа для пользователя.
Используйте декоратор @check_admin для проверки уровня доступа

ACCOUNTS = {
    "user123": "user",
    "luke23": "user",
    "alex1606": "user",
    "vaider_dart": "admin"
}
"""


def check_admin(function):
    pass


@check_admin
def log_in(name):
    pass


log_in("user")