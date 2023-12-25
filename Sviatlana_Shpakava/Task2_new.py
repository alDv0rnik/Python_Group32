# Task 2
def do_twice(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res1 = func(*args, **kwargs)
        return res, res1
    return wrapper

@do_twice
def add_2(x):
    return x + 2


print(*add_2(6))
