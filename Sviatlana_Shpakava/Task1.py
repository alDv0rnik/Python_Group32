fib1 = fib2 = 1
number = int(input())
number = int(number) - 2
while number > 0:
    fib_sum = fib1 + fib2
    fib1, fib2 = fib2, fib1 + fib2
    number = number - 1
print(fib2)
