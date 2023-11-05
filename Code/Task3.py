"""
Дано целое положительное число N. Вывести все числа Фибоначчи до числа, большего N.
Вывод чисел запиши через пробел.
"""

n = int(input())

fib1 = fib2 = 1
print(fib1, fib2, end=" ")
while fib2 <= n:
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=" ")
