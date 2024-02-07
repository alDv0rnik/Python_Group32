"""
Реализовать программу-напоминание с таймером (Timer).
Программа должна спрашивать: "О чём вам напомнить?" и "Через сколько минут (секунд)?"
По прошествии указанного времени нужно вывести заданный текст.
Дополните функционал программы работой с потоком.

Пример работы программы:

О чём вам напомнить?
Попить воды
Через сколько секунд?
20
Пока поток работает, мы можем сделать что-нибудь ещё
Попить воды
"""
import time
from threading import Thread, Timer


# def remind_me(msg: str, time_to_sleep: int) -> None:
#     print("Пока поток работает, мы можем сделать что-нибудь ещё")
#     time.sleep(time_to_sleep)
#     print(msg)
#
#
# def threaded(msg: str, time_to_sleep: int):
#     thread = Thread(
#         target=remind_me, args=(msg, time_to_sleep, )
#     )
#     thread.start()
#     thread.join()


def remind_me(msg: str):
    print(msg)


def threaded(msg: str, time_to_sleep: int):
    worker = Timer(
        time_to_sleep, remind_me, args=(msg, )
    )

    worker.start()
    print("Пока поток работает, мы можем сделать что-нибудь ещё")
    worker.join()


if __name__ == '__main__':
    prompt = input("О чём вам напомнить? ")
    time_ = int(input("Через сколько секунд? "))
    threaded(prompt, time_)






