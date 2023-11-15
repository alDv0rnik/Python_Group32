s = "some_string"
i = 5
l = [1, 2, 3]
t = (1, 2, 3)

# print(dir(l))
print(hash(s))
print(hash(i))
# print(hash(l))
print(hash(t))


d5 = {
    1: "int",
    1.0: "float",
    True: "bool"
}

print(hash(1))
print(hash(1.0))
print(hash(True))