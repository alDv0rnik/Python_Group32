from .base_car import BaseRailcar
from math import pi


class Tank(BaseRailcar):
    def __init__(self):
        self.__name = "tank"
        self.__radius = 1.25
        self.__length = 6
        self.__weight = 38.8
        self.__max_weight = 108
        self.__vol = self.__calculate_vol()

    def __calculate_vol(self):
        return pi * pow(self.__radius, 2) * self.__length

    def get_vol(self):
        return self.__vol

    def load_cargo(self, material):
        self.__weight += self.get_vol() * material.get_density()

    def get_weight(self):
        return round(self.__weight / 1000, 2)

    def __repr__(self):
        return f"{self.__name}: {self.get_weight()} tons"
