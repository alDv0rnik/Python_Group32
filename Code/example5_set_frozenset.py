# Sets
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
print(A.union(B))


# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)
print(A.intersection(B))

# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)
print(A.difference(B))


# Frozensets
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})

# difference
print(A.difference(B))  # Output: frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})