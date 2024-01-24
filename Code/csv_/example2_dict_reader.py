import csv

with open('data/example1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)

    for line in reader:
        # print(line)
        print(int(line.get("price")))