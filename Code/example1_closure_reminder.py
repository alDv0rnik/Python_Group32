# Вызов функции внутри другой функции.

def foo(name):
    print(f"My name is {name}")


def bar(func: object) -> None:
    func("Misha")


bar(foo)
