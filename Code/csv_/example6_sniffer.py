import csv

# создаем экземпляр класса Sniffer для дальнейшего использовании при
# сканировании структур файлов

sniffer = csv.Sniffer()
dialect = None

with open("data/undefined_dialect.csv", "r") as file:
    data = file.read()
    dialect = sniffer.sniff(data)

print(dialect.delimiter, dialect.quotechar, dialect.quoting, ascii(dialect.lineterminator))

with open("data/undefined_dialect.csv", "r") as file:
    reader = csv.reader(
        file,
        dialect=dialect
    )

    for line in reader:
        print(line)