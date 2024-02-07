import multiprocessing as mp


def creator(data_: list, q_: mp.Queue) -> None:
    for d in data_:
        print(f"Send element {d} to q:")
        q_.put(d)


def consumer(q: mp.Queue) -> None:
    while not q.empty():
        processed = q.get()
        print(f"From q: {processed ** 2}")
        # return processed ** 2


if __name__ == '__main__':
    q = mp.Queue()
    data = [x for x in range(1, 10)]

    worker1 = mp.Process(
        target=creator, args=(data, q,)
    )
    worker2 = mp.Process(
        target=consumer, args=(q,)
    )
    worker1.start()
    worker2.start()

    q.close()
    q.join_thread()

    worker1.join()
    worker2.join()

