# Task 4
from collections import OrderedDict
dct = OrderedDict({1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"})
firstelem = list(dct.items())[0]
lastelem = list(dct.items())[-1]
dct.move_to_end(firstelem[0])
dct.move_to_end(lastelem[0], last = False)
secondelem = list(dct.items())[1]
del dct[secondelem[0]]
dct["new_key"] = "new_value"
print(dct)
print(id(dct))
