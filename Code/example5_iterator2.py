from collections.abc import Iterator, Iterable


class MyIterator:
    pass


class MyIterable:
    pass


l = MyIterable()

for i in l:
    print(i)

print(isinstance(MyIterator(), Iterator))
print(isinstance(MyIterable(), Iterable))
print(isinstance(MyIterable(), Iterator))
print(isinstance(l, Iterable))
