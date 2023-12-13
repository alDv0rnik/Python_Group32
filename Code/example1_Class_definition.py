### Class definition (Class Person, method tell_name)
import time

class MyClass:
    def __new__(cls, *args, **kwargs):
        print(args)
        print("Inside __new__ method")
        return super().__new__(cls)

    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def get_attr(self):
        print(self.x)


# my_class1 = MyClass(1)
# my_class2 = MyClass(2, 4)
# print(my_class1.x)
# print(my_class1.y)
# my_class2 = MyClass()
# print(MyClass.a)

# my_class1.set_attr(1, 2)
# my_class1.get_attr()

class Person:
    def __init__(self, name):
        self.name = name

    def tell_name(self):
        return f"My name is {self.name}"

    def __del__(self):
        print(f"Delete object {self.name}")


person_1 = Person("Nick")
person_2 = Person("Jane")

print(person_1.tell_name())
del person_1
time.sleep(2)









