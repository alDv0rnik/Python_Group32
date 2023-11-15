# add()
a = set()
a.add(1)
a.add(6)
a.add((1, 3))
print(a)

# copy(), clear()


# discard(), remove(), pop()
a.discard(6)
print(a)
a.discard(4)
print(a)

a.remove(1)
print(a)

p = a.pop()
print(a, p)

# NO indexes
b = {1, 2, 2, 3, 4, 4}
# print(b[0])

set1 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}
set2 = {4, 5, 6, 7}

# set1.update(set2)
# set1 |= set2
print(set1)

# UNION
# print(set1.union(set2))

# INTERSECTION
# print(set1.intersection(set2))
# print(set1 & set2)

# DIFF
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1 - set2)

# print(set1.symmetric_difference(set2))

print(set1 == set3)
print(set1 < set2)
print(set1 > set3)

print(set1.issuperset(set3))
print(set3.issubset(set1))
print(set3.isdisjoint(set2))

print({i for i in range(5)})

set4 = frozenset([1, 2, 3, 4])
set_empty = frozenset()
# set4.add(6)
# set4.pop()
print(set4)
print(set_empty)

print(1 in set4)
