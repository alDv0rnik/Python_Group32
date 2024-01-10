from enum import Enum

from .base_factory import BaseFactory


class RailcarType(Enum):
    PLATFORM = "platform"
    TANK = "tank"
    CONTAINER = "container"


class RailcarFactory(BaseFactory):

    def create(self, railcar_type):
        railcar = self.__get_railcar(railcar_type)
        return railcar()

    def __get_railcar(type_: str):
        if type_ == RailcarType.TANK.value:
            return Tank
        elif type_ == RailcarType.CONTAINER.value:
            return Container
        elif type_ == RailcarType.PLATFORM.value:
            return Platform
        else:
            return "Not implemented class"