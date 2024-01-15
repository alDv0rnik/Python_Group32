from .base_car import BasePlatform


class Platform(BasePlatform):
    def __init__(self):
        self.__name = "platform"
        self.__weight = 12
        self.__limit = 2
        self.__cargo = []

    def get_weight(self):
        return self.__weight

    def load_cargo(self, cargo):
        if len(self.__cargo) < self.__limit:
            self.__cargo.append(cargo)
            self.__weight += cargo.get_weight()
        else:
            print("Out of limit")

    def get_cargo_view(self):
        return self.__cargo

    def __repr__(self):
        return f"{self.__name}: {self.__weight} tons"