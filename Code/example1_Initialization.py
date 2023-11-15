d = {
    "one": 1,
    "two": 2,
    "three": 3
}

d1 = dict(a=1, b=2, c=3)  # через dict() и ключевые аргументы
d2 = dict([("a", 1), ("b", 2)])  # через dict() и список кортежей
d3 = dict.fromkeys(("a", "b", "c"), 100)  # через fromkeys()
d4 = {a: b**2 for a, b in enumerate(range(5))}  # через dict comprehension

print(d)
print(d1)
print(d2)
print(d3)
print(d4)

# Keys must be unique
heroes = {"name": "Batman", "name1": "Robin"}
print(heroes)

# >>>> ?
d5 = {
    1: "int",
    1.0: "float",
    True: "bool"
}
# print(d5)


dct = {("a", ["b"]): 12}
print(dct)