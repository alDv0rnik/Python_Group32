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


class Hero(BaseUnit):
    def __init__(self, name, team):
        super().__init__()
        self.__name = name
        self.__team = team
        self.__level = 0

    @property
    def team(self):
        return self.__team

    @property
    def name(self):
        return self.__name

    def level_up(self):
        self.__level += 1


class Soldier(BaseUnit):

    @property
    def team(self):
        return self.__team

    def set_team(self):
        self.__team = random.choice(TEAMS)

    @staticmethod
    def follow_the_hero(hero: Hero) -> str:
        return f"Following {hero.name}"


def main():
    hero_1 = Hero("Iron Man", "red")
    print(f"I'm {hero_1.name}, {hero_1.id}")
    hero_2 = Hero("Cap", "blue")
    print(f"I'm {hero_2.name}, {hero_2.id}")
    reds, blues = [], []

    for i in range(10):
        soldier = Soldier()
        soldier.set_team()
        if soldier.team == "red":
            reds.append(soldier)
        else:
            blues.append(soldier)

    if len(reds) > len(blues):
        hero_1.level_up()
        print(f"NEW LEVEL! for {hero_1.name}")
    elif len(reds) < len(blues):
        hero_2.level_up()
        print(f"NEW LEVEL! for {hero_2.name}")

    print("Follow your hero!")
    soldier_1 = random.choice(reds)
    print(soldier_1.follow_the_hero(hero_1))
    print(soldier_1.id)
    print(hero_1.id)


if __name__ == '__main__':
    main()

# base_unit = BaseUnit()
# base_unit1 = BaseUnit()
# print(base_unit.id)
# print(base_unit1.id)

