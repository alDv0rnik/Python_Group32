import multiprocessing as mp
from multiprocessing.dummy.connection import Connection


def generate_list(conn: Connection):
    list_nums = [x for x in range(1, 11)]
    conn.send(list_nums)
    conn.close()


if __name__ == '__main__':
    receiver, sender = mp.Pipe(duplex=True)

    worker = mp.Process(
        target=generate_list, args=(sender, )
    )
    worker.start()

    res = receiver.recv()
    print(res)

    worker.join()
    receiver.close()

