from time import time
# Task 1
def timer(func):
    def wrapper(*args):
        start_time = time()
        result = func(*args)
        end_time = time()
        print("Время выполнения программы: ", end_time - start_time)
        return result
    return wrapper

@timer
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(5))
