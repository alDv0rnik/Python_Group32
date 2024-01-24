import csv

with open('data/example1.csv', "r") as file:
    # print(file.read())
    reader = csv.reader(file)
    print("Lines number: ", reader.line_num)
    print("Dialect: ", reader.dialect)

    for line in reader:
        print("Lines number: ", reader.line_num)
        print(line)