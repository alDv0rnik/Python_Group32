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
ACCOUNTS = {
    "user123": "user",
    "luke23": "user",
    "alex1606": "user",
    "vaider_dart": "admin"
}


def check_admin(function):
    def wrapper(*args, **kwargs):
        if args[0] in ACCOUNTS:
            print(ACCOUNTS[args[0]])
            function(args[0])
    return wrapper


@check_admin
def log_in(name):
    pass


log_in("user123")