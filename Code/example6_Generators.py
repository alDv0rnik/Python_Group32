def my_gen(num):
    while num > 0:
        yield "+"
        num -= 1

g = my_gen(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

