from collections.abc import Iterable, Iterator

l = [1,2,3]
li = iter(l)

print(type(l))
print(type(li))

# print(next(l))

print(next(li))
print(next(li))
print(next(li))
print(next(li))

class MyIterator:
    def __iter__(self):
        return self
#
print(isinstance(l, Iterator))
print(isinstance(li, Iterator))

for i in l:
    print(i)

print(dir(l))
print(dir(li))
