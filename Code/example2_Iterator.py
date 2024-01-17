from collections.abc import Iterable, Iterator

lst = [1, 2, 3]

iter_lst = iter(lst)

# print(dir(lst))
# print(dir(iter_lst))

# print(next(iter_lst))
# print(next(iter_lst))
# print(next(iter_lst))
# print(next(iter_lst))

# print(len(iter_lst))
# print(iter_lst[0])

class MyIter:
    def __iter__(self):
        return self


mi = MyIter()
print(isinstance(mi, Iterator))
print(isinstance(mi, Iterable))

# for i in lst:
#     print(i)