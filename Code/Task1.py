"""
Написать iterator-класс, который будет возвращать квадрат числа
в диапазоне 0 до 20, и связанный с ним  iterable-класс,
который будет возвращать итератор
"""


class SquareNumsIterator:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num > 19:
            raise StopIteration
        return self.num ** 2


class SquareNumsIterable:
    def __iter__(self):
        return SquareNumsIterator()


square_nums = SquareNumsIterable()
for i in square_nums:
    print(i)