"""
сравнение выполнения вычислений в разных потоках и в одном основном потоке
GIL
"""
from threading import Thread
import time


# def calc(n):
#     res = 0
#     for i in range(1, n):
#         for j in range(1, n):
#             res += i ** j
#
#
# def sequence(n):
#     for i in range(n):
#         calc(300)
#     print(f"{n} iterations are done!")
#
#
# if __name__ == '__main__':
#     started = time.time()
#     sequence(80)
#     end = time.time() - started
#     print(f"Execution time: {end}")

# 80 iterations are done!
# Execution time: 8.281803607940674


def calc(n, x, thread):
    res = 0
    for i in range(1, n):
        for j in range(1, n):
            res += i ** j
    print(f"Iteration #{x}. Thread {thread} ")


def sequence(n, thread):
    print(f"Run thread {thread}")
    for i in range(n):
        calc(300, i, thread)
    print(f"{n} iterations are done!")


def threaded(num_of_threads, n):
    threads = []

    for thread in range(num_of_threads):
        t = Thread(target=sequence, args=(n, thread))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    started = time.time()
    threaded(4, 80)
    end = time.time() - started
    print(f"Execution time: {end}")

