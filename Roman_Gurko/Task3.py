def func(x):
    m = {k: 1 for k in x}
    return list(m.keys())


print(func([1, 6, 15, 35, 4, 1, 15, 6]))