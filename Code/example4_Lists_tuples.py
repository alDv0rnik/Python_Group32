import sys


lst = list(range(10))
# lst1 = list()
# print(id(lst1))
# del lst1
# lst2 = []
# print(id(lst2))

print(lst)
print(lst[1])
print(lst[::-1])
print(lst[11:])

# s = "test"
# print(s[:4])


lst[5] = 'a'
print(lst)
lst[15:15] = 'b'
lst[8:10] = 'c'
print(lst)

lst[5:8:2] = 'v', 'f'
print(lst)

print(id(lst[1]), id(1))


tpl = ()
lst5 = []

print(sys.getsizeof(tpl))
print(sys.getsizeof(lst5))


t1 = (1, 2, 3)
print(id(t1))
del t1

t2 = (1, 2, 3)
print(id(t2))
