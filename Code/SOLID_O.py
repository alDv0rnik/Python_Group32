"""
классы, модули должны быть открыты для расширения, но закрыты для модификации
"""
from abc import ABC


class Shape:
    pass


class BaseShape(ABC):
    pass