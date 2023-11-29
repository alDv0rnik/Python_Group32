def recursive_max_comm_div(a, b):
    if a < b:
        return b if not a else recursive_max_comm_div(b % a, a)
    else:
        return a if not b else recursive_max_comm_div(b, a % b)


def iterable_max_comm_div(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print(recursive_max_comm_div(320, 17))
print(iterable_max_comm_div(320, 17))