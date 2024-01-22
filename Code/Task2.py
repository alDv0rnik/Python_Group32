"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
Протестируем функцию на файле «cars.txt» со следующим содержимым:

TeslaLuxury Electric Vehicles2003-Present
BMWLuxury Vehicles1916-Present
FerrariLuxury Sports Cars1947-present.
FordMass-Market Cars1903-Present
PorscheLuxury Sports Cars1931-Present
HondaMass-Market Cars1948-Present
LamborghiniLuxury Sports Cars1963-Present
ToyotaMass-Market Cars1937-Present
"""

file_path = "cars.txt"


def read_lines(lines: int, file: str) -> list:
    with open(file, "r") as file_:
        list_of_cars = list(map(lambda x: x.strip("\n"), file_.readlines()))
        return list_of_cars[-lines:]


print(*read_lines(3, file_path), sep="\n")
