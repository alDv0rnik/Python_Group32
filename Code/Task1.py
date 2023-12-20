"""
Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои.
У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде.
У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой".
У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.

Отправьте одного из солдат первого героя следовать за ним.
Выведите на экран идентификационные номера этих двух юнитов.
"""
import random
import uuid


TEAMS = ["red", "blue"]


class BaseUnit:
    def __init__(self):
        self.__id = self.set_id()
        self.__team = None

    @property
    def id(self):
        return self.__id

    @property
    def team(self):
        return self.__team

    @staticmethod
    def set_id():
        return str(uuid.uuid4())


class Soldier(BaseUnit):

    @property
    def team(self):
        return self.__team

    def set_team(self):
        self.__team = random.choice(TEAMS)

    @staticmethod
    def follow_the_hero(hero: object) -> str:
        return f"Following {hero.name}"


sold = Soldier()
sold.set_team()
print(sold.id)
print(sold.team)

# base_unit = BaseUnit()
# base_unit1 = BaseUnit()
# print(base_unit.id)
# print(base_unit1.id)

