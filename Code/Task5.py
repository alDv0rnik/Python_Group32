"""
1. Написать класс автомобиля с атрибутами марки, цвета и объема двигателя и
методами: ехать вперед и ехать назад.
2. Написать класс автомобиля, унаследованного от первого класса в пункте 1.
Добавить методы поворота налево и направо.
3. Написать класс самолета, имеющего метод взлетать и атрибут модель самолета.
4. Написать класс, унаследованный  от машины (2 пункт) и от самолета (3 пункт).
Посмотреть что будет.
"""


class BaseCar:
    def __init__(self, brand, color, vol):
        self.brand = brand
        self.color = color
        self.vol = vol

    def drive_forward(self):
        return "Drive forward"

    def drive_backward(self):
        return "Drive backward"


class Car(BaseCar):

    def turn_right(self):
        return "Turning right"

    def turn_left(self):
        return "Turning left"


class Plane:
    def __init__(self, model):
        self.model = model

    def take_off(self):
        return "Taking off"


class PlaneCar(Car, Plane):
    def __init__(self, brand, color, vol, model):
        Car.__init__(self, brand, color, vol)
        Plane.__init__(self, model)


print(PlaneCar("BMW", "red", 1.8, "Boeing").take_off())
