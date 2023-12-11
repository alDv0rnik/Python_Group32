def get_div(a, b):
    if b != 0:
        return round(a / b, 2)
    raise ZeroDivisionError
