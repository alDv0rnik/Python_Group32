import csv

def read_csv():
    with open("data.csv") as file:
        keys = file.readline().strip().split(",")
        return [dict(zip(keys, line.strip().split(","))) for line in file]


print(read_csv())
