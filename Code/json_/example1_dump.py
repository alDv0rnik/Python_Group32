import json

dct = {
    "name": "Ivan",
    "numbers": [1, 2, 3],
}


with open("data.json", "w") as file:
    json.dump(dct, file)

with open("data.json", "r") as file:
    data = json.load(file)
    print(type(data))

dct_str = json.dumps(dct)
print(dct_str)
print(dct_str[:5])

dct_ = json.loads(dct_str)
print(type(dct_))
