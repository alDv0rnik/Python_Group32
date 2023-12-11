# This is a new module

# define some objects here
a = 54
b = "text"

lst = [1, 2, 3, 4]

def show_arg(arg):
    return f"arg ={arg}"

class SomeClass:
    pass

# print(a, b)

# entrypoint goes here
if __name__ == "__main__":
    print(f"File __name__ set to {__name__}")
    print("This is mod file")
    print(a, b)


# shhow the difference between script and import __name__
# print(f"File __name__ set to {__name__}")