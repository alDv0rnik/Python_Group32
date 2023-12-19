"""
Создайте класс рабочий Worker и задайте ему три атрибута: name, job, salary
Сделайте salary приватным. Напишите методы getters и setters для данного атрибута
Либо используйте декоратор property
"""


# class Worker:
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         self.__salary = value
#
#
# worker = Worker("Jane", "teacher", 1000)
# print(worker.salary)
# worker.salary = 1500
# print(worker.salary)  # worker.set_salary(1500)

class Worker:
    salary_map = {
        "A": 1500,
        "B": 1000,
        "C": 500
    }

    def __init__(self, class_):
        self.__salary = self.__return_salary(class_)

    @property
    def salary(self):
        return self.__salary

    def __return_salary(self, class_: str) -> int:
        return self.salary_map.get(class_, 0)


worker = Worker("A")
print(worker.salary)
