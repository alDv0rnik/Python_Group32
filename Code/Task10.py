"""
Дан список чисел [1, 1, 4, 5, 1, 2, 1]. Убрать из списка все дубликаты
"""
from copy import copy

# print([i for i in range(10) if i % 2 == 0])


lst = [1, 1, 4, 4, 4, 5, 5, 1, 2, 1]
res = []

# for elem in lst:
#     if elem not in res:
#         res.append(elem)
# print(res)

# INPLACE ALGORITHM
first = 0
second = 0

#!!!!! Список должен быть сортированным
lst.sort()
print(lst)

while first < len(lst):
    while second < len(lst) - 1 and lst[second] == lst[second + 1]:
        second += 1

    lst[first] = lst[second]
    first += 1
    second += 1

    if second == len(lst):
        print(lst[:first])
        break

print(lst)
