from abc import ABC


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape = shape_type
        if self.shape == "circle":
            self.radius = kwargs["radius"]
        if self.shape == "rectangle":
            self.length = kwargs["length"]
            self.width = kwargs["width"]

    def calculate_area(self):
        if self.shape == "circle":
            return 3.14 * self.radius ** 2
        if self.shape == "rectangle":
            return self.length * self.width


shape_1 = Shape("circle", radius=3)
print(shape_1.calculate_area())
shape_2 = Shape("rectangle", width=5, length=6)
print(shape_2.calculate_area())


class BaseShape(ABC):

    def calculate_area(self):
        pass


class Rectangle(BaseShape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width

