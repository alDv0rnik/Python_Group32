class User:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if type(age) is int and age >= 0:
            self.__age = age


u = User(15)
u.set_age(-1)
print(u.get_age())
u.set_age("1")
print(u.get_age())
u.set_age(1)
print(u.get_age())

