d = {
    "one": 1,
    "two": 2,
    "three": 3
}

d1 = 0 # через dict() и ключевые аргументы
d2 = 0 # через dict() и список кортежей
d3 = 0 # через fromkeys()
d4 = 0 # через dict comprehension

print(d)
print(d1)
print(d2)
print(d3)
print(d4)

# Keys must be unique


# >>>> ?
d5 = {
    1: "int",
    1.0: "float",
    True: "bool"
}
# print(d5)
