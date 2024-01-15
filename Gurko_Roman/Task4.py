class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        pass

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы должны быть числом')

    @property
    def kg(self):
        return self.__kg


cls = KgToPounds(20)
print(cls.kg)
cls.set_kg(40)
print(cls.kg)
