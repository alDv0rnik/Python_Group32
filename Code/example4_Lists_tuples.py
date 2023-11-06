lst = list(range(10))
print(id(lst))
print(id(lst[1:5]))

lst1 = lst[1:5]
print(id(lst1))

a = []
b = []

print(a is b)

lst[11:11] = 'a', 'b', 'c'
print(lst)

lst[5] = 'r'
print(lst)

print(lst[15:])
print(id(lst[1]))
print(id(1))
