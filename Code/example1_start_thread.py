import threading
from time import sleep

WORK = True


def handler(name: str, time: int):
    while WORK:
        print(f"The {name} thread start to sleep {time} sec")
        sleep(time)


worker1 = threading.Thread(
    target=handler,
    args=("first", 2)
)
worker2 = threading.Thread(
    target=handler,
    args=("second", 3)
)

worker1.start()
worker2.start()

sleep(5)

print("Stop programm")
WORK = False