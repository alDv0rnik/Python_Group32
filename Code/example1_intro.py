class Dog:
    def voice(self):
        print("Woof")


class Cat:
    def voice(self):
        print("Meow")


cat = Cat()
dog = Dog()

instances = [cat, dog]
for instance in instances:
    instance.voice()
