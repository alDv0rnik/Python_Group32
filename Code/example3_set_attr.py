class SomeClass:
    __slots__ = ('a', '_SomeClass__b')

    def __init__(self, a, b=9):
        self.a = a
        self.__b = b

    def some_method(self):
        pass

    # def __setattr__(self, key, value):
    #     if key in ('a', '_SomeClass__b'):
    #         self.__dict__[key] = value
    #     else:
    #         raise AttributeError


sc = SomeClass(1)

sc.a = 2
print(sc._SomeClass__b)
sc.c = "test"
# sc.b = 5
# print(sc.__dict__)
print(sc.__slots__)
# sc2 = SomeClass(57)
# print(sc2.__dict__)

