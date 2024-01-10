from enum import Enum
from .base_factory import BaseFactory


class RailcarType(Enum):
    PLATFORM = "platform"
    TANK = "tank"
    CONTAINER = "container"


class RailcarFactory(BaseFactory):
    def create(self, railcar_type):
        railcar = self.__get_railcar(railcar_type)
        return railcar

    @staticmethod
    def __get_railcar(type_: str):
        if type_ == RailcarType.PLATFORM.value:
            return Platform
        elif type_ == RailcarType.TANK.value:
            return Tank
        elif type_ == RailcarType.CONTAINER.value:
            return Container
        else:
            return "Not implemented class"
