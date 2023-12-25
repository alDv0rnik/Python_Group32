# Task 3
def call_once(func):
    cash = []
    def wrapper(*args, **kwargs):
        nonlocal cash
        cash.append(func(*args, **kwargs))
        return cash[0]
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 43))
print(sum_of_numbers(999, 100))
