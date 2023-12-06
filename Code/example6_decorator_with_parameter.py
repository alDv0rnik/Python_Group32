from decorators import slowdown


@slowdown(rate=1)
def count(num):
    print(num)
    if num < 1:
        return num
    return count(num - 1)


count(6)

