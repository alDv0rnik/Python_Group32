class Soda:
    def __init__(self, topping=None):
        self.__topping = topping

    def show_my_drink(self):
        return f"Газировка с {self.__topping}ом" if self.__topping else "Вода с газом"


s_with = Soda("вишневый топпинг")
print(s_with.show_my_drink())
s_without = Soda()
print(s_without.show_my_drink())
