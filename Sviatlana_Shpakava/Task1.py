with open("unsorted_names.txt", "r") as names:
    name = sorted(names.read().split("\n"))
    name = "\n".join(name)
    print(name)

with open("sorted_names.txt", "w") as file:
    file.write(name)
