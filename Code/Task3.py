"""
Написать класс Rectangle, который имеет 2 аргумента width и length (ширина и длина)
и метод get_area, который возвращает площадь прямоугольника с такими  сторонами.
Унаследовать от него класс Square, переопределить метод get_area как произведение
ширины на ширину (или длины на длину).

"""

class Rectangle:
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "length"):
            self.__dict__["width"] = value
            self.__dict__["length"] = value


square = Square(5)
square.width = 7
print(square.__dict__)
print(square.get_area())