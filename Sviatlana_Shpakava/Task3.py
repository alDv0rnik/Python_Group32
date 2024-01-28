class Figure:

    def __init__(self, shape, side_a, side_b):
        self.shape = shape
        self.side_a = side_a
        self.side_b = side_b

    def get_square(self):
        return self.side_b * self.side_b


class Rectangle(Figure):

    def __init__(self, shape, side_a, side_b, length, height):
        super().__init__(shape, side_a, side_b)
        self.__length = length
        self.__height = height

    def rectangle_square(self):
        if isinstance(self.__length, int) and isinstance(self.__height, int):
            return self.__length * self.__height
        raise TypeError

    def set_length_height(self, value_1, value_2):
        if value_1 > 0:
            self.__length = value_1
        if value_2 > 0:
            self.__height = value_2
        else:
            raise AttributeError

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height


try:
    shape_rectangle = Rectangle("rectangle", 2, 2, 3, "ttt")
    print(shape_rectangle.rectangle_square())
except TypeError:
    print("Несоответствие типов данных")

try:
    shape_rectangle = Rectangle("rectangle", 2, 2, 3, 5)
    print(shape_rectangle.rectangle_square())
    print(shape_rectangle.set_length_height(6, 0))
    print(shape_rectangle.rectangle_square())
except AttributeError:
    print("Ошибка атрибута")
