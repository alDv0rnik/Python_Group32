"""
классы, модули должны быть открыты для расширения, но закрыты для модификации
"""
from abc import ABC
from math import pi


class Shape:
    def __init__(self, **kwargs):
        self.type = None
        if kwargs['type'] == 'circle':
            self.type = kwargs['type']
            self.radius = kwargs['radius']
        if kwargs['type'] == 'square':
            self.type = kwargs['type']
            self.a = kwargs['a']

    def calculate_area(self):
        if self.type == 'circle':
            return pi * self.radius ** 2
        if self.type == 'square':
            return self.a * self.a


class BaseShape(ABC):

    def calculate_area(self):
        pass


class Circle(BaseShape):
    def __init__(self, radius):
        self.type = 'circle'
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Square(BaseShape):
    def __init__(self, a):
        self.type = 'square'
        self.a = a

    def calculate_area(self):
        return self.a * self.a

    def __str__(self):
        return f"Calculated area: {self.calculate_area()}"


