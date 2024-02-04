import csv

class MyOwnDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "/"
    quotechar = "-"
    lineterminator = "\r"


csv.register_dialect("my_dialect", dialect=MyOwnDialect)

with open("mydialect.csv", "w") as fl:
    writer = csv.writer(
        fl,
        dialect="my_dialect"
    )
    writer.writerow(["hello", "my", "dear", "friend"])
    writer.writerow([999, 888, 777, 666])
    writer.writerow(["wow", "wOw", "WoW", "WOW"])
    writer.writerow([555, 444, 333, 222])

with open("mydialect.csv", "r", newline="") as fl_:
    reader = csv.reader(
        fl_,
        dialect="my_dialect"
    )
    for row in reader:
        print(",".join(row))
