# Адресация в памяти
import sys


str_1 = "Hello world"
print(type(str_1.encode()))
print(str_1, id(str_1))
str_2 = "Hello world"
print(str_2, id(str_2))
d = "d"
str_1 = "Hello worl" + d
print(str_1, id(str_1))

str_ = ""
str_3 = str()

print(sys.getsizeof(str_3))

# ASCII
letter = "P"
# print(bin(ord(letter)))
# print(chr(89))
#
# print("P" > "Y")


# Экранирование
str_4 = 'don\'t'
# print(repr(str_4))

str_5 = """Hi,
my
name
is
Alex"""

# print(repr(str_5))
# print(str_5)

# Управляющие конструкции

str_6 = "ab\'c"
print(str_6)
print(len(str_6))

