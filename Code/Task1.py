"""
Написать 2 асинхронные функции:
1 - генерирует случайное число в диапазоне от 100 до 1000
2 - возводит числа в куб
в main необходимо получить сумму из 10 чисел через gather()
"""
import asyncio
import random


async def generate_num():
    return random.randint(100, 1000)


async def get_cubes():
    res = await generate_num()
    return pow(res, 3)


async def main():
    tasks = []

    for i in range(10):
        task = asyncio.create_task(get_cubes())
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    return sum(results)


if __name__ == '__main__':
    print(asyncio.run(main()))
