# append
lst = list(range(5))
print(lst)
#
# lst.append(6)
# print(lst)
#
# lst = []
# for i in range(5):
#     lst.append(i)
#     print(lst)


# clear
# lst.clear()
# print(lst)

# count
# lst.append(4)
# print(lst.count(4))


# extend
# t = "text"
# s = list(t)
# print(s)

# lst1 = ['a', 'b']
# lst.extend(lst1)
# print(lst)

# index
lst1 = ['a', 'b', 1, 1, 2, 4, 5, 5, 6]
# print(lst1.index('a', 3, 5))

# insert
lst1.insert(3, 'c')
print(lst1)

# tpl1 = (1, 2, 3)
# tpl1.insert(2, 'c')

# pop

elem = lst1.pop(4) # index = -1
print(lst1)
print(elem)

# remove
lst1.remove(5)
print(lst1)

# sort
lst2 = [9, 5, 1, 3, 4, 6, 2, 8, 7]
lst2.sort(reverse=False, key=lambda x: x % 2 == 0) # sorted
# lst3 = sorted(lst2)
print(lst2)

tpl1 = (9, 5, 1, 3, 4, 6, 2, 8, 7)
print(sorted(tpl1))

