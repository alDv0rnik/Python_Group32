"""
exception-hierarchy
"""

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

print("Hello world")

a = 10
b = 0

# print(a/b)

i = input("Введите число ")
if isinstance(i, str):
    raise ValueError("Wrong value")
else:
    print(i)