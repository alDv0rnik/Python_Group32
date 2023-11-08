"""
Создайте список, состоящий из N элементов, которые указываются функцией ввода данных.
Первым вводом укажи размер списка (N), далее — элементы списка.
Требуется найти наименьший нечётный элемент данного списка, если такого элемента нет — вывести 0.
"""

lst = [int(input()) for _ in range(int(input()))]

# res = []
# for elem in lst:
#     if elem % 2 != 0:
#         res.append(elem)
# print(min(res) if res else 0)

# print(min([elem for elem in [int(input()) for _ in range(int(input()))] if elem % 2 != 0]))
# print(*filter(lambda x: x % 2 != 0, lst))
