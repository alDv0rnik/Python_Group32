from .base_cargo import BaseCargo


class Steel(BaseCargo):
    def __init__(self):
        self.__name = "steel"
        self.__density = 7700 # kg per m3

    def get_density(self):
        return self.__density

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"{self.__name}"
