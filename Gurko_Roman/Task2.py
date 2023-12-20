def do_twice(func):
    def wrapper(*args, **kwargs):
        res_1 = func(*args, **kwargs)
        res_2 = func(*args, **kwargs)
        return res_1, res_2
    return wrapper


@do_twice
def get_sum(*args):
    return sum(args)


res1 = get_sum(1, 2, 3, 4, 5)
print(*res1)