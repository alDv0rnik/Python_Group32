from abc import ABC, abstractmethod


class BaseRailcar(ABC):

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_vol(self):
        pass

    @abstractmethod
    def load_cargo(self, *args):
        pass


class BasePlatform(ABC):

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def load_cargo(self, *args):
        pass