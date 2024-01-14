class Tomato:

    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working!')

    def harvest(self):
        print('Gardener is harvesting!')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Tomato is not ripe yet!')

    @staticmethod
    def knowledge_base():
        print('''Справка по садоводству. Бла бла... бла бла...''')

TomatoBush = TomatoBush(9)
Gardener = Gardener('Tomas', TomatoBush)
Gardener.knowledge_base()
Gardener.work()
Gardener.harvest()
TomatoBush.all_are_ripe()
TomatoBush.give_away_all()
Gardener.harvest()
