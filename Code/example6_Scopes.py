# a = [1, 2, 3]
# b = 2
# c = 'abc'
# d = sorted(a)
#
#
# def foo():
#     tmp = 0
#
#
# print(dir())

# name = "Tomas"
#
# def say_hello():
#     name = "Bob"
#     print(locals())
#     print(globals())
#     return f"Hello {name}!"
#
#
# def say_bye():
#     return f"Bye {name}"
#
#
# print(say_hello())
# print(say_bye())
#
#
# for i in range(10):
#     print(i)
#
#
# print(globals())



# name = "Tomas"
#
#
# def say_hello():
#     global name
#     name = "Bob"
#     return f"Hello {name}!"
# #
# #
# def say_bye():
#     return f"Bye {name}"
#
#
# print(say_hello())
# print(say_bye())


# n = 78
#
# def outer():
#     # n = 6
#
#     def inner():
#         # nonlocal n
#         n = 16
#         print("inner", n)
#
#         def inner_inner():
#             global n
#             n = 18
#             print("inner_inner", n)
#
#         inner_inner()
#         print("inner", n)
#
#     inner()
#     print("outer", n)
#
# outer()


GLOBAL = 99

def bar(i):
    GLOBAL = i
    return GLOBAL

#
# print(bar(100))


# def a():
    # print(x)


# def b():
#     x = 45
#     a()


# b()