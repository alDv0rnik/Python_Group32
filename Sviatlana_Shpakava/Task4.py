def fibo(n):
    fibo1, fibo2 = 0, 1
    for _ in range(n):
        yield fibo1
        fibo1, fibo2 = fibo2, fibo1 + fibo2

gen = fibo(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
