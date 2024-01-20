"""
Re-raise explanation or raise from
"""
# try:
#     # from math import s1
#     f = open("test.txt")
#     s = f.read()
# except FileNotFoundError:
#     print("error1")
# except ImportError as err:
#     print(err)
#     raise


try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error") from None



