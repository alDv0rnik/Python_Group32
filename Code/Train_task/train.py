class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Train(metaclass=SingletonMeta):
    def __init__(self):
        self.__capacity = 1500
        self.__cars = []

    def get_cars(self):
        return self.__cars

    def add_car(self, railcar):
        self.__cars.append(railcar)

    def __summarize(self):
        sum_weight = sum([railcar.get_weight() for railcar in self.__cars])
        return sum_weight

    def is_able_to_ride(self):
        return self.__summarize() <= self.__capacity


# train = Train()
# train1 = Train()
#
# print(id(train))
# print(id(train1))
