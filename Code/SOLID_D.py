"""
DIP. абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций
"""
from abc import ABC


class FrontEnd:
    def __init__(self, backend):
        self.backend = backend

    def display(self):
        data = self.backend.get_data()
        return f"Data from DB {data}"


class DataSource(ABC):

    def get_data(self):
        pass


class Database(DataSource):

    def get_data(self):
        return "Data from DB"


class API(DataSource):

    def get_data(self):
        return "Data from API"


