def num_generator(n):
    for i in range(n):
        yield i


num_gen = num_generator(3)
# print(dir(num_gen))
#
# print(next(num_gen))
# print(next(num_gen))
# print(next(num_gen))
# print(next(num_gen))

gen = (i for i in range(5))
lst = [i for i in range(5)]
print(*gen)
# print(lst)

print(type(gen))
print(type(lst))