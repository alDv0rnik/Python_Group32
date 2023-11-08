"""
При помощи выражения list comperhension создать список кортежей, которые включают в себя первые значения от 1 до 10.
Вторые от 10 до 1 в виде строки.

"""
print([(i, str(11-i)) for i in range(1, 11)])
print([(i, str(10-j)) for i, j in enumerate(range(1, 11), start=1)])


l1 = [n for n in range(1, 11)]
l2 = [str(n) for n in range(10, 0, -1)]
print(list(zip(l1, l2)))


l3 = [1, 2, 3, 4]
l4 = [5, 6, 7]

print(list(zip(l3, l4)))


