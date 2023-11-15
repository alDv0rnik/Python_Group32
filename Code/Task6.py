"""
Удалите из словаря d = {1: 1, '2': 2, '3': 3, 4: 4} все элементы со строковыми ключами.
"""
from copy import deepcopy

d = {1: 1, '2': 2, '3': 3, 4: 4}
d_copy = d.copy()

# for k in d_copy:
#     if isinstance(k, str):
#         d.pop(k)
# print(d)

print({k: v for k, v in d.items() if not isinstance(k, str)})
