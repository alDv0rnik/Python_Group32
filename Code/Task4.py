"""
Попробуйте самостоятельно перегрузить оператор сложения. Используйте метод __add__.
Метод __add__ может возвращать что угодно.
В нашем случае метод перегрузки сложения будет возвращать новый объект того же класса,
где в качестве аргумента будет сумма, полученная в результате вызова метода __add__.

Пример.
a = A(2)
b = a + 3
print(b)        ->  5
print(type(b))  ->  <class '__main__.A'>
"""


class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return A(self.a + other)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.a == other

    def __str__(self):
        return str(self.a)


a = A(5)
b = a + 2
print(a == 5)

print(b)
print(type(b))