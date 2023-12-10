# Task 2
def do_twice(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        print(result)
    return wrapper

@do_twice
def add_2(x):
    return x + 2


print(add_2(6))
