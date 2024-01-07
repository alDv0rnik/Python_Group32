dictionary = []
class UserDict:

    def __init__(self, key):
        self.key = key

    def set_value(self, key, value):
        self.value = value
        dictionary.append(key)

    def get_history(self):
        return dictionary

d = UserDict({"a", 1})
d.set_value("b", 2)
d.set_value("c", 3)
d.set_value("d", 4)
d.set_value("e", 5)
d.set_value("f", 6)
d.set_value("g", 7)
print(d.get_history())
