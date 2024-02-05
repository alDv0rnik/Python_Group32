"""
Реализовать класс MoneyBox с методами deposit и withdraw. В каждом методе должны присутствовать
механизмы блокировки потока lock. Также реализовать класс пользователь (наследуется от Thread) и переопределить
в нем метод run. На вход классу подаются 2 атрибута - имя пользователья и операция,
которую он совершает (deposit или withdraw). Задача  блокировать возможность выполннения операции во время ее использования
другим пользователем.
"""
from threading import Thread, Lock
import time


class MoneyBox:

    def __init__(self):
        self.amount = 50
        self.lock = Lock()

    def deposit(self, num=10):
        with self.lock:
            print("Money in the box: ", self.amount)
            self.amount += num
            time.sleep(1)
            print("Deposit has been made")

    def withdraw(self, num=10):
        with self.lock:
            print("Money in the box: ", self.amount)
            time.sleep(2)
            if self.amount < num:
                print("No more money in the box")
            else:
                self.amount -= num
                print("Withdraw has been made")


class User(Thread):
    def __init__(self, name, operation, money_box):
        super().__init__(name=name)
        self.name = name
        self.operation = operation
        self.money_box = money_box

    def run(self):
        print(f"{self.name} try to make {self.operation}")
        oper = getattr(money_box, self.operation)
        oper()
        print(f"{self.name} made a {self.operation}")


money_box = MoneyBox()
user1 = User("Mike", "withdraw", money_box)
user1.start()

user2 = User("Ann", "deposit", money_box)
user2.start()


user1.join()
user2.join()

print("end")