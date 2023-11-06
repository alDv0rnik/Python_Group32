num = int(input('введите сколько чисел фибоначчи вывести  '))
fib1=0
fib2=1
print(fib1, fib2, end=" ")
while num>2:
    fib1, fib2 = fib2, fib1+fib2
    print(fib2, end=" ")
    num-=1
