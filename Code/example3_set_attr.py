class SomeClass:

    def __init__(self, a):
        # print(dir())
        self.a = a
        self.__x = a - 1

    # def get_names(self):
    #     print(dir())

    def __setattr__(self, key, value):
        # print(self.__dict__)
        if key in ('a', '_SomeClass__x'):
            self.__dict__[key] = value
        else:
            raise AttributeError

print(dir())
sc = SomeClass(4)
# sc.get_names()
print(sc.__dict__)
# sc.__x = 5
# print(sc.__dict__)
# sc.c = "test"
# print(sc.__dict__)