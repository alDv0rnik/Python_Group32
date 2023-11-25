# Task 3
def func(elem):
    d = {}
    for i in elem:
        if i in d:
            pass
        else:
            d[i] = True
    new_list = list(d.keys())
    return new_list


print(func([1, 15, 35, 4, 1, 15]))
