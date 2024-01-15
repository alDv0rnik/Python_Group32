from .base_car import BaseRailcar


class Container(BaseRailcar):

    def __init__(self):
        self.__name = "container"
        self.__height = 2
        self.__wight = 2.5
        self.__length = 6
        self.__weight = 20
        self.__max_weight = 70 # in tons
        self.__vol = self.__calculate_vol()

    def get_vol(self):
        return self.__vol

    def __calculate_vol(self):
        return self.__length * self.__height * self.__wight

    def get_weight(self):
        if (m := self.__weight / 1000) > self.__max_weight:
            return self.__max_weight
        return m

    def load_cargo(self, material):
        self.__weight += material.get_density() * self.__vol

    def __repr__(self):
        return f"{self.__name}: {self.get_weight()} tons"


