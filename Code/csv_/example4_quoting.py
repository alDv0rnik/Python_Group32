import csv

# Используем словари для записи в csv_ файл DictWriter
quoting = csv.QUOTE_NONNUMERIC

with open("data/output.csv", "w") as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=["fname", "lname", "age"],
        quoting=quoting,
        lineterminator="\n"
    )
    writer.writeheader()
    writer.writerow(
        {
            "fname": "Maxim",
            "lname": "Tank",
            "age": 40
        }
    )
    writer.writerow(
        {
            "fname": "Yakub",
            "lname": "Kolas",
            "age": 46
        }
    )