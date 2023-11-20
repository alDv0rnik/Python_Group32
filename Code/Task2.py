"""
Напишите программу которая принимает последовательность слов, разделенных запятой. Выведите на консоль
все уникальные слова в отсортированном виде
Methods: list, split
Вход:  red, white, black, red, green, black
Выход: black green red white
"""


def print_unique(*args):
    res = sorted(list(set(args)))
    return res


print(*print_unique("red", "white", "black", "red", "green", "black"))
