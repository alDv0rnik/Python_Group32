#Task 3
num = int(input('Введите трехзначное число '))
sum = num // 100 % 10 + num // 10 % 10 + num % 10
print(f'Сумма цифр числа {num} равна {sum}')
