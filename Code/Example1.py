import os
import time
from threading import Thread
import multiprocessing as mp

# print(os.cpu_count())
# print(os.getpid())


def calc(n, calc, proc):
    res = 0
    for i in range(1, n):
        for j in range(1, n):
            res += i ** j
    print(f"Iteration #{calc}. Thread {proc} ")


def sequence(n, proc):
    print(f"Run core {proc}")
    for i in range(n):
        calc(300, i, proc)
    print(f"{n} iterations are done!")


def processed(num_of_proc, calc):
    n_proc = num_of_proc if num_of_proc <= os.cpu_count() else os.cpu_count()
    n_calc = calc // n_proc
    procs = []

    for proc in range(n_proc):
        p = mp.Process(target=sequence, args=(n_calc, proc))
        procs.append(p)
        p.start()

    [pr.join() for pr in procs]


if __name__ == '__main__':
    started = time.time()
    processed(5, 80)
    end = time.time() - started
    print(f"Execution time: {end}")