spisok = []

class DefineType:

    def __init__(self, data, new_value):
        self.data = data
        self.new_value = new_value

    def define_this(self):
        if self.data == isinstance(self.data, set) or isinstance(self.data, list):
            spisok.append(self.new_value)
            return spisok
        elif self.data == isinstance(self.data, str):
            return self.data + self.new_value

d = DefineType([1, 2, 3], 13)
print(d.define_this())
d = DefineType([4, 5, 6], 15)
print(d.define_this())
d = DefineType("Hello", 111)
print(d.define_this())
