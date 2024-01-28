def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    if a < 0:
        raise ZeroDivisionError
    if a > 3:
        raise IndexError
    print(x, a, y)


def bar(a):
    result = foo(a)
    return result

try:
    result_bar = foo(0)
    print(f"Result of function bar: {result_bar}")
except ZeroDivisionError:
    print("Error of function bar: a must be > 0")


def bzz(a):
    result = bar(a)
    return result

try:
    result_bzz = bzz(3)
    print(f"Result of function bzz: {result_bzz}")
except IndexError:
    print("Error of function bzz: a must be < 2")
