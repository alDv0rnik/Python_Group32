import threading
import time
import random
from threading import Lock

# counter = 0
#
#
# def thread_job():
#     global counter
#     tmp = counter
#     time.sleep(random.randint(0, 1))
#     counter = tmp + 1
#     print(f"{counter}", end=" ")
#
#
# workers = [threading.Thread(target=thread_job) for _ in range(10)]
# for worker in workers:
#     worker.start()
#
# for worker in workers:
#     worker.join()


counter = 0
lock = Lock()


def thread_job():
    with lock:
        global counter
        tmp = counter
        time.sleep(random.randint(0, 1))
        counter = tmp + 1
        print(f"{counter}", end=" ")


workers = [threading.Thread(target=thread_job) for _ in range(10)]
for worker in workers:
    worker.start()

for worker in workers:
    worker.join()