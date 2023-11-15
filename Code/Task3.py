"""
Удалить все пары ключ-значение, значения которых начинается с буквы а.
"""

dct = {"1": "apple", "2": "microsoft", "3": "samsung", "4": "atari"}
print({k: v for k, v in dct.items() if not v.startswith('a')})

dct1 = dict()
for k, v in dct.items():
    if not v.startswith('a'):
        dct1[k] = v
