"""
Дан неотсортированный список чисел [9, 1, 5, 8, 3, 0, 2, 6, 5, 7]. Рассмотрим сортировку пузырьком.
O(n^2)
"""

lst = [9, 1, 5, 8, 3, 0, 2, 6, 5, 7]


for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] >= lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]


print(lst)