"""
ISP Клиентов не следует заставлять зависеть от методов, которые они не используют.
Интерфейсы принадлежат клиентам, а не иерархиям.
"""
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_(self, doc):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, doc):
        pass


class Scaner(ABC):
    @abstractmethod
    def scan(self, doc):
        pass


class OldPrinter(Printer):

    def print_(self, doc):
        return f"Print {doc}"


class MFD(Printer, Fax, Scaner):
    def print_(self, doc):
        return f"Print {doc}"

    def fax(self, doc):
        return f"Send Fax {doc}"

    def scan(self, doc):
        return f"Scan {doc}"
