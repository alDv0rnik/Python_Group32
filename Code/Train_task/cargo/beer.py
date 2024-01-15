from .base_cargo import BaseCargo


class Beer(BaseCargo):
    def __init__(self):
        self.__name = "beer"
        self.__density = 1040

    def get_density(self):
        return self.__density

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"{self.__name}"
