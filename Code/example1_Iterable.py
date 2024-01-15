from collections.abc import Iterable

l = [1,2,3]
s = "text"
dic = {1: 1, 2: 2}

print(isinstance(l, Iterable))
print(isinstance(s, Iterable))
print(isinstance(dic, Iterable))

print(dir(l))