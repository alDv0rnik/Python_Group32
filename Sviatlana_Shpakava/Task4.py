n = int(input("Проверка на простое число: "))
count = 0
for i in range(2, n):
    if n % i == 0:
        count = count + 1
if count <= 0:
    print("1")
else:
    print("0")
