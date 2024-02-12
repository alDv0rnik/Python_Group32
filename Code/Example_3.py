import asyncio


async def get_squares(num):
    await asyncio.sleep(1)
    return pow(num, 2)


async def get_cubes(num):
    await asyncio.sleep(2)
    return pow(num, 3)


async def main():
    task1 = asyncio.create_task(get_squares(7), name="Task 1")
    task2 = asyncio.create_task(get_cubes(2), name="Task 2")

    result = await asyncio.gather(task1, task2)
    # res1 = await task1
    # res2 = await task2
    #
    # print(type(task1))
    # print(task1.__class__.__base__)
    return result


if __name__ == '__main__':
    print(asyncio.run(main()))


    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(main())
    # print(result)
    # loop.close()