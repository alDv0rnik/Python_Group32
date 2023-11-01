# >, <, <=, >=, ==, !=, is, in, :=

# if условие:
#     операция
# else:
#     операция


# if условие1:
#     операция1
# elif условие2:
#     операция2
# else:
#     операция3


# if условие1:
#     операция1
# if условие2:
#     операция2
# else:
#     операция3

a = 1
b = None

print(a and b)

print(b or a)

print(0 or 100 or 2000)

# print(None and True or (None, False) and [False])

l = []
t = tuple()
d = dict()

# print(bool(l))
# print(bool(t))
# print(bool(d))

a = 0
if a:  # if True:
    y = 2
    print(y)

# print(y)

# day = input()

# в версии 3.10 и выше

# match day:
#     case "День":
#         print("Добрый день!")
#     case "Утро":
#         print("Доброе утро!")

# walrus operator

# dct_list = [
#     {"name": "John", "age": 26},
#     {"name": "Sam", "age": 34}
# ]
#
# for item in dct_list:
#     name = item.get("name")
#     if name:
#         print(name)
#
#
# for item in dct_list:
#     if name := item.get("name"):
#         print(name)
#
# num = 1
# print("ok" if num > 0 else "not ok")


# Вхождение

lst = [1, 2, 3, 4]
a = 5
print(a in lst)
print(a not in lst)

text = "test"
chr = "t"
print(chr in text)