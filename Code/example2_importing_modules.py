# import mod
# from mod import SomeClass, some_function, foo
# from mod import *
import mod as m


### NameError occuring
# print(mod.a)
# print(mod.some_function(1, 2, 3))

# s = SomeClass()
# print(s)
# print(some_function(1, 2, 3))
# print(foo())

print(m.a)


### Overwrite existing variables

m.a = 15
print(m.a)




