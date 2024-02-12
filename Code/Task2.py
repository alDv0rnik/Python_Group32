"""
Написать программу, в которой есть официант и повар (2 корутины).
Официант принимает заказы (создает задачу), а повар их выполняет.

Вывод программы:
Новый заказ - пицца
Новый заказ - салат
Новый заказ - паста

Заказа готовиться
Заказа готовиться
Заказа готовиться

Пицца готова
Салат готов
Паста готова
"""
import asyncio
from enum import Enum


class TimeToCook(Enum):
    PASTA = 3
    PIZZA = 4
    SALAD = 2


async def waiter(order: str):
    task1 = asyncio.create_task(cook("Pasta"))
    task2 = asyncio.create_task(cook("Pizza"))
    task3 = asyncio.create_task(cook("Salad"))

    await task1
    await task2
    await task3


async def cook(order: str):
    cooking_time = 0
    if order == "Pasta":
        cooking_time = TimeToCook.PASTA.value
    elif order == "Pizza":
        cooking_time = TimeToCook.PIZZA.value
    elif order == "Salad":
        cooking_time = TimeToCook.SALAD.value
    print(f"Cooking {order} {cooking_time} secs")
    await asyncio.sleep(cooking_time)
    print(f"{order} ready")


asyncio.run(waiter())
