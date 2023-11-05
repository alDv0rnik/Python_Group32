from typing import Iterable

my_range = range(1, 10, 2)
text = "asdbfef"
text1 = 123

print(my_range.start)
print(my_range.stop)
print(my_range.step)


# print(dir(text))
# print(dir(text1))
# print(isinstance(text, Iterable))

# print(type(my_range))
# print(dir(my_range))
#

#
it = iter(my_range)
print(type(it))
print(dir(it))
# #
# #
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print(len(my_range))
# print(len(it))

print(my_range[2])
# print(it[2])

