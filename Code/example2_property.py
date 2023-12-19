"""
Обработка приватного поля через геттер и сеттер. Определение атрибута как свойства класса.
Используем синтетический пример User
"""

class User:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        print("call set method")
        self.__name = name

    def get_name(self):
        print("call get method")
        return self.__name

    # name = property(get_name, set_name)


user = User("Nick")
# print(user.get_name())
# user.set_name("Mike")
# print(user.get_name())
# print(user.name)
print(user.name)
user.set_name("Mike")
# print(user.name)