"""
Пусть надо написать программу, вычисляющую площади разных фигур.
Пользователь указывает, площадь какой фигуры он хочет вычислить.
После этого вводит исходные данные.
Например, длину и ширину в случае прямоугольника.
Чтобы разделить поток выполнения на несколько ветвей, следует использовать оператор if-elif-else
Methods: if-else, input, functions
Input: "1-прямоугольник, 2-треугольник, 3-круг:" 1
        "Ширина: " 2
        "Высота: " 6
Output: "Площадь: " 12
"""


def get_area_triangle(a, h):
    return (a * h) / 2


def get_area_rectangle(a, b):
    return a * b


def get_area_circle(r, pi=3.14):
    return pi * pow(r, 2)


def main():
    n = input("1-прямоугольник, 2-треугольник, 3-круг: ")
    if n == "1":
        a = int(input("Ширина: "))
        b = int(input("Длина: "))
        print("Площадь: ", get_area_rectangle(a, b))
    elif n == "2":
        a = int(input("Сторона: "))
        h = int(input("Высота: "))
        print("Площадь: ", get_area_triangle(a, h))
    else:
        r = int(input("Радиус: "))
        print("Площадь: ", get_area_circle(r))


if __name__ == '__main__':
    main()
