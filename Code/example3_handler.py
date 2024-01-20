"""
try-except explanation
"""

# try:
#     a = int(input("First number: "))
#     b = int(input("Second number: "))
#     res = a / b
# except ValueError as error:
#     print(f"A value error occurred: {error}")
# except ZeroDivisionError as error_:
#     print(f"ZeroDivisionError: {error_}")
# except Exception:
#     print("Unexpected error")
# else:
#     print(f"Division result: {int(res)}")
# finally:
#     print("close program")


try:
    file = open("test.txt", "r")
    strings = file.read()
except (FileNotFoundError, NameError, AttributeError) as err:
    print(err)
else:
    file.close()
    print(strings)



