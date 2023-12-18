class TestClass:
    count = 0

    def __init__(self, new_attr=0):
        self._new_attr = new_attr
        print()


print(TestClass().count)
print(TestClass()._new_attr)

test = TestClass(10)
print(test._new_attr)
print(dir())

