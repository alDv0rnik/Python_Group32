import os
import time
import multiprocessing as mp


def calc(n, calc, proc):
    res = 0
    for i in range(1, n):
        for j in range(1, n):
            res += i ** j
    print(f"Iteration #{calc}. Process: {proc} ")


def sequence(n, proc):
    print(f"Run core {proc}")
    for i in range(n):
        calc(300, i, proc)
    print(f"{n} iterations are done!")


def pooled(calc, core=None):
    n_proc = core if core <= os.cpu_count() else os.cpu_count()
    num_calc = calc // n_proc
    inti_seq = [(num_calc, x) for x in range(n_proc)]

    with mp.Pool(n_proc) as pool:
        pool.starmap(sequence, inti_seq)

    return n_proc, num_calc, core


if __name__ == '__main__':
    start = time.perf_counter()
    n_proc, calc, n_cores = pooled(80, 4)
    end = time.perf_counter() - start

    print(f"Number of cores used: {n_cores}")
    print(f"Number of calculations per core: {calc}")
    print(f"Total iterations: {n_proc * calc}. Elapsed time: {end}")