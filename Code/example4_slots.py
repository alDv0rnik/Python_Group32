class SomeClass:
    __slots__ = ['a', '_SomeClass__x']

    def __init__(self, a):
        # print(dir())
        self.a = a
        self.__x = a - 1

    # def get_names(self):
    #     print(dir())

    # def __setattr__(self, key, value):
    #     # print(self.__dict__)
    #     if key in ('a', '_SomeClass__x'):
    #         self.__dict__[key] = value
    #     else:
    #         raise AttributeError


sc1 = SomeClass(10)
# print(sc1.__dict__)
print(sc1.__slots__)
sc1.c = "test"