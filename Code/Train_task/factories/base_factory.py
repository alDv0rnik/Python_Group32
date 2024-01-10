from abc import ABC, abstractmethod


class BaseFactory(ABC):

    @abstractmethod
    def create(self, *args):
        pass