"""
Напишите функцию split_by_index(s: str, indexes: List[int]) -> List[str],
которая делит строку по переданным индексам.

Неправильные индексы должны быть проигнорированы

split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]
"""
from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    start = 0
    res = []
    for index in indexes:
        if index > len(s):
            continue
        res.append(s[start:index])
        start = index
    res.append(s[start:])
    return res


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18, 21]))
print(split_by_index("no luck", [42]))
# s = "pythoniscool,isn'tit?"
# print(s[23])