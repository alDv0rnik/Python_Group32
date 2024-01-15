class MyIterator:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 0:
            self.num -= 1
            return "+"
        else:
            raise StopIteration


l = MyIterator(3)
# for i in l:
#     print(i)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
