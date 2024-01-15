from collections.abc import Iterator, Iterable


class MyIterator:
    def __init__(self):
        self.num = 0
        self.res = ""

    def __iter__(self):
        return self

    def __next__(self):
        self.res += "*"
        if self.num > 10:
            raise StopIteration
        self.num += 1
        return self.res


class MyIterable:
    def __iter__(self):
        return MyIterator()


l = MyIterable()

for i in l:
    print(i)

print(isinstance(MyIterator(), Iterator))
print(isinstance(MyIterable(), Iterable))
print(isinstance(l, Iterable))
