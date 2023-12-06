# Простой декоратор на принтах


def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("---Before decoration ---")
        func(*args, **kwargs)
        print("---After decoration---")
    return wrapper


@my_simple_decorator
def say_name(f_name: str, l_name: str) -> None:
    print(f"My name {f_name} {l_name}")


# foo = my_simple_decorator(say_name)
# foo("John", "Connor")

say_name("John", "Connor")
