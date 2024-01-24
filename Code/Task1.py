"""
Создайте  функцию,  которая  будет  создавать  CSV  файл  на  основе  данных,  введенных
пользователем  через  консоль.  Файл  должен  содержать следующие  колонки:  имена,  фамилии,
возраст и  город  проживания.

Ввод данных производить в одну строку через пробел
"""
import csv

HEADERS = ["fname", "lname", "age", "city"]
QUOTING = csv.QUOTE_NONNUMERIC


def create_csv():
    with open("names.csv", "w") as file:
        writer = csv.writer(file, quoting=QUOTING, lineterminator = "\n")
        writer.writerow(HEADERS)
        while True:
            n = input()
            if n == "q":
                break
            else:
                writer.writerow(n.split())


if __name__ == '__main__':
    create_csv()