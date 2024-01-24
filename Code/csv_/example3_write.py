import csv

with open('data/output.csv', 'w') as f:
    quoting = csv.QUOTE_NONNUMERIC
    writer = csv.writer(f, quoting=quoting, lineterminator="\n")
    writer.writerow(["a", "b", "c", "d"])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([5, 6, 7, 8])
    writer.writerow([9, 10, 11, 12])
