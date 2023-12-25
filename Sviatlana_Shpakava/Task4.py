class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    @property
    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы должны быть числом')

    def get_kg(self):
        return self.__kg

weight1 = KgToPounds(100)
print(weight1.to_pounds)
weight1.set_kg(500)
print(weight1.get_kg())
weight1.set_kg(1000)
print(weight1.get_kg())
print(weight1.to_pounds)
weight1.set_kg('hello')
