N = int(input("Enter your number: "))
fib1 = 0
fib2 = 1
for i in range(N - 1):
    fib1, fib2 = fib2, fib1 + fib2
print("Your Fibonachi number is", fib1)
