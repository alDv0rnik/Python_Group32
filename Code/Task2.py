"""
Выполнить отправку 10 запросов на https://www.python.org/
в виде обычной функции и разделив на потоки.
Результаты запросов response.status_code сохранить в виде списка.
Для отправки запросов испрпользовать библиотеку requests
"""
import time
from threading import Thread

import requests
from requests import RequestException

urls = ["https://www.python.org/"] * 10


def make_request(url_):
    resp = requests.get(url_)
    if resp.ok:
        return resp.status_code
    raise RequestException


def threaded():
    threads = []

    for url in urls:
        t = Thread(target=make_request, args=(url, ))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    started = time.time()
    threaded()
    # for url in urls:
    #     print(make_request(url))
    end = time.time() - started
    print(f"Execution time: {end}")
    # Execution time: 7.143199920654297
    # Execution time: 1.6432223320007324
