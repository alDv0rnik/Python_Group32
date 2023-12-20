import time


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return res
    return wrapper


@timer
def fibo(num):
    s1 = 1
    s0 = 0
    if num == 2:
        return s1
    if num > 2:
        for i in range(num - 1):
            s0, s1 = s1, s0 + s1
    return s0


print(fibo(int(input())))
