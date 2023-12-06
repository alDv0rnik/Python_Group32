import time
from functools import wraps


def debug_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        This is wrapper
        :param args:
        :param kwargs:
        :return:
        """
        args_list = [str(arg) for arg in args]
        kwargs_list = [f"{k}={v}" for k, v in kwargs.items()]
        seq_ = ", ".join(args_list + kwargs_list)
        print(f"Calling function {func.__name__} with args: {seq_}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned result: {result}")

        return result
    return wrapper


def slowdown(rate=0.1):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            time.sleep(rate)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator_function


def timer(function):
    pass