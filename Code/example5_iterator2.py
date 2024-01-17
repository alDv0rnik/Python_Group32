from collections.abc import Iterator, Iterable


class MyIterator:
    pass


class MyIterable:
    pass


l = MyIterable()

for i in l:
    print(i)
