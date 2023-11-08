import math
N = int(input("Enter your number: "))
res = 1
for i in range(2, N):
    res += pow(-1, i+1) * math.factorial(i)
print(res)
