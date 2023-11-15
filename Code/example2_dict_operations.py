d = {
    "one": 1,
    "two": 2,
    "three": 3
}
d1 = {
    "four": 4
}

print(len(d))

# UNION
# dct = d | d1
# print(dct)
# d.update(d1)
# print(d)
# dct = {**d, **d1}
# print(dct)

# a = d.keys() | {'four', 'five'}
# b = d.values() | {4, 5} # TypeError
# print(a)
# print(b)

# ITERATING
for item in d:
    print(item)


for val in d.values():
    print(val)


# print(type(d.items()))

for key, val in d.items():
    print(key, "-> ", val)
