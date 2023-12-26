"""
Реализуйте класс Car, который будет иметь приватный атрибут name_speed_dict,
содержащий информацию о марке автомобиля и его
максимальной скорости и max_speed.
Класс должен содержать два метода define_max_speed(name) и distance_time_on_max_speed(distance).
Используя перегрузку метода distance_time_on_max_speed выведите время,
за которое авто проедет указанное расстояние.

car = Car(name="BMW")
"""


class Car:
    def __init__(self, name: str):
        self.__name_speed_dict = {
            "bmw": 250,
            "nissan": 200
        }
        self.__max_speed = self.__define_max_speed(name)

    def __define_max_speed(self, name):
        return self.__name_speed_dict.get(name.lower(), 0)

    def distance_time_on_max_speed(self, dist):
        if not self.__max_speed:
            return "Speed is not defined"
        return round(dist / self.__max_speed, 2)


car = Car(name="BMW")
print(car.distance_time_on_max_speed(100))
