class Soda:

    def __init__(self, topping=None):
        self.topping = topping

    def show_my_drink(self):
        if self.topping:
            print(f'Газировка с {self.topping}')
        else:
            print('Вода с газом')

drink_first = Soda()
drink_second = Soda('пуншем')
drink_third = Soda('вишенкой')
drink_first.show_my_drink()
drink_second.show_my_drink()
drink_third.show_my_drink()
