"""
Create Custom exceptions (raise...from)
"""


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"Custom exception raised {self.msg}"


try:
    f = open("test1.txt")
    s = f.read()
except Exception as err:
    raise CustomException("No such file") from err