def fun(a: list) -> list[tuple]:
    if len(a) == 1:
        return None
    b = a.pop(0)
    if type(a[0]) is tuple:
        return a
    a.append((b, a[0]))
    return fun(a)


print(fun(['need', 'to', 'sleep', 'more']))
