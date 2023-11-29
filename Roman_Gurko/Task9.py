def foo(a: list[int]) -> list[int]:
    b = []
    for i in range(len(a)):
        c = 1
        for j in range(len(a)):
            if j != i:
                c *= a[j]
        b.append(c)
    return b


print(foo([1, 2, 3, 4, 5]))
