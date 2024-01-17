"""
Напишите класс-итератор, объекты которого:
а) генерирует целые числа в количестве и в диапазоне, которые передаются в конструктор
б) генерируют случайные числа в том же диапазоне.
"""
import random


class RandomIterator:
    def __init__(self, min, max, n):
        self.min = min
        self.max = max
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return random.randint(self.min, self.max)


class StepIterator:
    def __init__(self, min, max, n):
        self.min = min
        self.max = max
        self.n = n
        self.step = (self.max - self.min) // n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        self.min += self.step
        return self.min


step_iter = StepIterator(5, 20, 5)
rand_iter = RandomIterator(5, 20, 5)

for i in step_iter:
    print(i, end=" ")

print()
for i in rand_iter:
    print(i, end=" ")
