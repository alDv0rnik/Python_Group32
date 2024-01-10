"""
подтипы должны быть взаимозаменяемыми для своих базовых типов.
"""
from SOLID_O import BaseShape


class Rectangle(BaseShape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


class Square(BaseShape):
    def __init__(self, a):
        self.a = a

    def calculate_area(self):
        return self.a * self.a


# class Sqaure(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         if key in ("a", "b"):
#             self.__dict__["a"] = value
#             self.__dict__["b"] = value

def get_area(*args):
    sum_area = sum([a.calculate_area() for a in args])
    return sum_area


s = Square(5)
r = Rectangle(3, 4)
print(s.calculate_area())
print(r.calculate_area())

print(get_area(s, r))


