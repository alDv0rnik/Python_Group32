from threading import Thread
from time import sleep
import time


def calculate_squares(start, end):
    res = 0
    for i in range(start, end):
        res += i ** 2
    print("Result: ", res)


task = Thread(target=calculate_squares, args=(1, 10000000,))
started_at = time.time()
print("RESULT 1")
task.start()
task.join()
end = time.time() - started_at

print(f"Executed time: {end}") # Executed time: 2.375157356262207

started_at = time.time()
print("RESULT 2")
calculate_squares(1, 10000000)
end = time.time() - started_at
print(f"Executed time: {end}")
