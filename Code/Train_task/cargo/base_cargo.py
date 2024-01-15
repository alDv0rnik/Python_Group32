from abc import ABC, abstractmethod


class BaseCargo(ABC):

    @abstractmethod
    def get_density(self):
        pass


class BaseItem(ABC):

    @abstractmethod
    def get_weight(self):
        pass