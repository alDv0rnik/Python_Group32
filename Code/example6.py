"""
Написать класс Person с атрибутами name, age. Возраст должен иметь валидное значение в
диапазоне от 1 до 100. Вызвать пользовательское исключение, если возраст невалиден.
Если возраст правильный то вызываем метод show_info()
"""


class PersonAgeError(Exception):
    def __init__(self, given_age, min_age, max_age):
        self.given_age = given_age
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return f"Not valid age {self.given_age}. Age value must be between {self.min_age} and {self.max_age}"


class Person:
    def __init__(self, name, age):
        self.name = name
        min_age_limit, max_age_limit = 1, 100
        if min_age_limit <= age <= max_age_limit:
            self.age = age
        else:
            raise PersonAgeError(age, min_age_limit, max_age_limit)

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}"


try:
    person1 = Person("John", 20)
    print(person1.show_info())
    person2 = Person("Bob", -1)
    print(person2.show_info())
except (PersonAgeError, TypeError) as e:
    print(e)



