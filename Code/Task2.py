"""
Напишите декоратор @double_it,
который возвращает удвоенный результат вызова декорированной функции

@double_it
def multiply(num1, num2):
    return num1 * num2

@double_it
def get_sum(*args):
    return sum(args)

res = get_sum(1, 2, 3, 4, 5)
print(res) # печатает 30
"""


def double_it(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res * 2
    return wrapper

@double_it
def get_sum(*args):
    return sum(args)


@double_it
def get_factorial(num):
    # print(num)
    if num == 1:
        return num
    return num * get_factorial(num - 1)


# res = get_sum(1, 2, 3, 4, 5)
# print(res)

print(get_factorial(5))