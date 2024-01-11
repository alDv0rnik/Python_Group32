from math import pi

default_radius = 5


def circle_perimeter(r=default_radius):
    return round(2 * pi * r, 2)


def circle_area(r=default_radius):
    return round(pi * r ** 2, 2)
