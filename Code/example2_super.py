"""
Define class Person - the parent class.
Define class Student to be inherited from Person.
Use super() method.
"""


class Person:
    def __init__(self, f_name="Joe", l_name="Doe"):
        self._f_name = f_name
        self.l_name = l_name

    def say_name(self):
        return f"My name is {self._f_name} {self.l_name}"


class Student(Person):
    def __init__(self, f_name="Joe", l_name="Doe", spec=None): # можно поставить *args
        super().__init__(f_name, l_name)
        self.spec = spec

    def say_name(self):
        return f"My name is {self._f_name} {self.l_name}. I'm a student.  I like {self.spec}"


student = Student(spec="Python")
print(student.say_name())

# class ITStudent(Student):
#
#     def say_name(self, spec=None):
#         return f"My name is {self.f_name} {self.l_name}. I'm a student. I like {spec}"
#
#
# student = ITStudent("Joe", "Doe")
# print(student.say_name("Python"))