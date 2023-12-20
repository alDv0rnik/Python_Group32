def call_once(func):
    res = []
    def wrapper(*args, **kwargs):
        nonlocal res
        res.append(func(*args, **kwargs))
        return res[0]
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(999, 100))