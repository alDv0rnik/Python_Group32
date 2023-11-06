num = int(input("Введите целое число"))
if (num > 0): answer = f"Положительное {len(str(num))} значное число"
elif (num < 0): answer = f"Отрицательное {len(str(num))} значное число"
else: answer = "Это ноль"
print(answer)
