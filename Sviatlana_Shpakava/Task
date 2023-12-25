class User:

    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def getter(self):
        return self.__age

    def setter(self, value):
        if value > 0:
            self.__age = value
        else:
            raise AttributeError

user1 = User("Kevin", 24)
print(user1.getter())
user1.setter(33)
print(user1.getter())
user1.setter(16)
print(user1.getter())
user1.setter(0)
print(user1.getter())
