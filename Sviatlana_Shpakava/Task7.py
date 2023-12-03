# Task 7
def nod(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a)


print(nod(5, 7))

def recursion_nod(a, b):
    if b == 0:
        return a
    else:
        return recursion_nod(b, a % b)


print(recursion_nod(5, 7))
