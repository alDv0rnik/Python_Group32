class HistoryDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__history = []

    def set_value(self, key, value):
        self[key] = value
        self.__history.append(key)
        if len(self.__history) > 10:
            self.__history.pop(0)

    def get_history(self):
        return self.__history


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())
print(d)