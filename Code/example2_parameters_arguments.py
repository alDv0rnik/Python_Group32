def calculate_area(r, pi=3.14):
    return pi * pow(r, 2)


print(calculate_area(5, 3.18))

### ARGUMENTS WRONG POSITION

# print(calculate_area(pi=3.18, 5))


def foo(a, b, c=None):
    print(a)
    print(b)
    print(c)

# foo(1, 2, 3)


### *args - arguments - tuple!
def get_sum(a, b, c, d):
    return sum([a, b, c, d])


def get_sum1(*args):
    return sum(args)


print(get_sum(1, 2, 3, 4))
print(get_sum1(1, 2, 3, 4, 5, 56, 8))
print(get_sum1())


### kwargs - key word arguments - dict
values = {
    "a": 1,
    "b": 2
}


def get_another_sum(**kwargs):
    sum_ = 0
    for k, v in kwargs.items():
        sum_ += v
    return sum_


print(get_another_sum(a=1, b=2))
print(get_another_sum(**values))


def bar(a, b, c=0, *args, d=100, **kwargs):
    pass

# bar(10, 5, 1, 2, 3, 4, 5, d=12, c=10, e=19)

def func(*args, **kwargs):
    pass


### PEP 570
def func1(a, b, c, /):
    return a + b + c


print(func1(1, 2, 3))


#### TYPE HINTING

def get_sum2(a: list[int], b: int) -> list[int] | None:
    """
    This function returns list of integer
    :param a: List of int
    :param b: Integer form 0 to 100
    :return: List
    """
    a.append(b)
    return a


print(get_sum2([5], 4))


