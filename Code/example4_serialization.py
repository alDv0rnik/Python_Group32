'''
Сериализация - это способ преобразования структуры данных в линейную форму,
которую можно сохранить или передать по сети.
'''
import pickle
import json

lst = ["abc", 14, 12.35]

with open("data.dat", "wb") as file:
    pickle.dump(lst, file)

with open("data.dat", "rb") as file:
    data = pickle.load(file)
    print(data)

data_ = pickle.dumps(lst)
print(data_)


test_dict = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9},
]

with open("data.json", "w") as file:
    json.dump(test_dict, file)


with open("data.json", "r") as file:
    data = json.load(file)
    print(data)