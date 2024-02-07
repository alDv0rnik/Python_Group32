import os
from multiprocessing import Pool


def generate_squares(num):
    res = num ** 2
    return res


def processed(core):
    data = [5, 10, 15, 12, 7]

    with Pool(core) as pool:
        res = pool.map(generate_squares, data)

    return res


if __name__ == '__main__':
    print(processed(4))
