import asyncio


async def foo():
    pass


@asyncio.coroutine
def get_squares(num):
    return pow(num, 2)


def get_cubes(num):
    return pow(num, 3)


def main():
    res1 = get_squares(7)
    res2 = get_cubes(10)
    return [res1, res2]


if __name__ == '__main__':
    print(main())