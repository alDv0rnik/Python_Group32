# Task 5
num = int(input("Введите число"))
summa = 0
prfac = 1
for i in range (1, num+1):
    prfac = prfac * i
    if i % 2 == 0:
        summa = summa + prfac * -1
    else: summa = summa + prfac
print(summa)
