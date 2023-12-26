"""
Method Overloading,
a way to create multiple methods with the same name but different arguments,
is not possible in Python
"""


class Counter:
    def __init__(self, a: int) -> None:
        self.a = a

    def calculate(self, x, exp=None, mult=None):
        if exp and not mult:
            return self.a ** x
        elif not exp and mult:
            return self.a * x
        elif exp and mult:
            return self.a ** x * x
        else:
            return self.a


counter = Counter(4)
print(counter.calculate(2, exp=True, mult=True))