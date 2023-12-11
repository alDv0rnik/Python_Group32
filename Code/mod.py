a = 10
b = 25.5


def some_function(*args):
    return sum(args)


def foo():
    return a + b


class SomeClass:
    pass


# if __name__ == "__main__":
print(f"The mod file name is {__name__}")