from enum import Enum

from cargo.beer import Beer
from cargo.steel import Steel
from cargo.tractor import Tractor
from factories.base_factory import BaseFactory


class CargoType(Enum):
    STEEL = "steel"
    BEER = "beer"
    TRACTOR = "tractor"


class CargoFactory(BaseFactory):

    def create(self, cargo_type):
        cargo = self.__get_cargo(cargo_type)
        return cargo()

    @staticmethod
    def __get_cargo(type_: str):
        if type_ == CargoType.STEEL.value:
            return Steel
        elif type_ == CargoType.BEER.value:
            return Beer
        elif type_ == CargoType.TRACTOR.value:
            return Tractor
        else:
            return "Not implemented class"

