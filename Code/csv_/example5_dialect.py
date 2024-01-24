import csv

# создание собственного диалекта для записи файла в csv_ через класс


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "|"
    quotechar = "*"
    lineterminator = "\r"


csv.register_dialect("test_dialect", dialect=MyDialect)

with open("data/output.csv", "w") as file:
    writer = csv.writer(
        file,
        dialect="test_dialect"
    )
    writer.writerow(["a", "b", "c", "d"])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([5, 6, 7, 8])
    writer.writerow([9, 10, 11, 12])
