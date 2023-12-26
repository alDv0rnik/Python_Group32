class Multiplier:
    def __init__(self, a: int):
        self.a = a

    def mult(self, x: int):
        self.a *= x

    def __str__(self): # __repr__
        return f"Current value {self.a}"


class Exponent(Multiplier):
    def mult(self, x: int):
        self.a **= x


mul = Multiplier(3)
exp = Exponent(3)

mul.mult(2)
exp.mult(2)

print(mul.a)
print(exp.a)

print(str(mul))
