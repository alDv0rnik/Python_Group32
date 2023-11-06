import math
a = int(input("Введите целое число"))
num = int(math.sqrt(a))
if num * num == a:
    print(a)
else: print("-1")
