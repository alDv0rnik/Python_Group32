# lambda arg: expression

def foo(x):
    return x ** 2


bar = lambda x: x ** 2
print(bar(2))
print(foo(2))


def func(x):
    return x / 0


# print(func(2))
# func1 = lambda x: x/0
# print(func1(2))


lst = list(range(10))
# print(list(map(lambda x: pow(x, 3), lst)))
# print(list(filter(lambda x: x % 2 != 0, lst)))

func2 = lambda x, y: x if x > y else y
# print(func2(5, 4))

nums = [lambda x=x: x * 2 for x in range(10)]
# for num in nums:
# print(num())

"""
Вход: 10591351
Выход: {5: 2, 1: 3, 3: 1}
"""
digits = "10591351"

from collections import Counter

counter = Counter(digits)
lst = {int(k): v for k, v in dict(counter).items()}
print(dict(sorted(lst.items(), reverse=True, key=lambda x: x[1])[:3]))
