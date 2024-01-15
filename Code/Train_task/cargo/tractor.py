from .base_cargo import BaseItem


class Tractor(BaseItem):
    def __init__(self):
        self.__name = "tractor"
        self.__weight = 4

    @property
    def name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def __repr__(self):
        return f"{self.__name}"
