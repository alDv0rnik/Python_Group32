from sys import getsizeof

a = []
b = {}
c = set()
d = frozenset()

print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
print(getsizeof(d))

lst = [1, 1, 2, 3, 5, 5, 5]
set_ = set(lst)
print(set_)

s = "kashkashdfs"
print(set(s))

dct = {"a": 1, "b": 2, "c": 3}
print(set(dct))


set1 = {"a", 1, 2, (1, 2)}
print(set1)
