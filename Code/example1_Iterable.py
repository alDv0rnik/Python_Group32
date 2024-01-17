from collections.abc import Iterable

l = [1, 2, 3]
d = 12
s = "text"
dic = {1: 1, 2: 2}

# print(dir(l))
# print(dir(d))

# print(isinstance(l, Iterable))
# print(isinstance(d, Iterable))

seq = range(5)
seq_iter = iter(seq)
print(dir(seq))
print(seq)
print(seq[0])
print(seq[3])

# print(seq_iter[3])
