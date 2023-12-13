"""
Написать класс автомобиля с атрибутами марки, цвета и объема двигателя и
методами: ехать вперед и ехать назад.

Все методы - это просто команда печати, например print(“Drive forward”)
"""


class Car:
    def __init__(self, model, color, vol):
        self.model = model
        self.color = color
        self.vol = vol

    def move_forward(self):
        return f"The car {self.model} is moving forward"

    def move_backward(self):
        return f"The car {self.model} is moving backward"


car1 = Car("bmw", "red", 1.8)
print(car1.move_forward())
print(car1.move_backward())