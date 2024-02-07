"""
Написать 2 функции, используя модуль multiprocessing.
1-я функция должна генерировать последовательность чисел в случайном порядке.
2-я - должна обрабатывать данные, переданные из очереди.
[1000, 1500, ...]
"""
import multiprocessing as mp
import os
import random


def generate_random_nums(start: int, end: int, q: mp.Queue):
    nums = [random.randint(start, end) for _ in range(random.randint(1, 10))]
    q.put(nums)


def processor(q: mp.Queue):
    while not q.empty():
        data = q.get()
        print(*map(lambda x: x ** 3, data))


def processed(queue, core=None):
    n_proc = core if core <= os.cpu_count() else os.cpu_count()
    procs = []

    extra_proc = mp.Process(
        target=processor, args=(q, )
    )

    for proc in range(n_proc - 1):
        p = mp.Process(
            target=generate_random_nums, args=(100, 100000, queue)
        )
        procs.append(p)
        p.start()

    extra_proc.start()

    [pr.join() for pr in procs]
    extra_proc.join()


if __name__ == '__main__':
    q = mp.Queue()
    processed(q, core=4)


