"""
напишите программу, которая работает также, как и метод split()
Использовать метод split запрещено
"""

sample = "This_is_a,test_string"
separator = "_,"
word = ""
res = []

for elem in sample:
    if elem not in separator:
        word += elem
    else:
        res.append(word)
        word = str()
print(res)
