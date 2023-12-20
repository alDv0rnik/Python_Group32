class A:
    def method_for_A(self):
        pass


class B(A):
    def __init__(self):
        print("b init")

    def method_for_B(self):
        pass

    def test(self):
        print("B class")


class C(B):
    def __init__(self):
        B.__init__(self)
        print("c init")

    def method_for_C(self):
        pass

    def test(self):
        print("C class")


class D(C, B):
    class_attr = 100

    def __init__(self):
        super().__init__()

    def method_for_D(self):
        pass


d = D()
print(D.__mro__)
print(issubclass(D, C))
print(issubclass(D, B))
print(issubclass(B, D))
