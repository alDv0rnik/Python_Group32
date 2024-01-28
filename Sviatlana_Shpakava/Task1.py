class MyOwnException(Exception):
    def __init__(self, val_a, val_b):
        self.val_a = val_a
        self.val_b = val_b

    def __str__(self):
        return f"Wrong value: a = {self.val_a}, b = {self.val_b}. Value a and b must be > 0"

def geometric(val_a, val_b):
    result = (val_a * val_b) ** 0.5
    if val_a < 0:
        raise MyOwnException(val_a, val_b)
    if val_b < 0:
        raise MyOwnException(val_a, val_b)
    return result

try:
    result = geometric(10, 10)
    print(f"Result of function: {result}")
except TypeError:
    print("Error! Enter number!")
except MyOwnException as error:
    print(error)
finally:
    print("Try once more")
