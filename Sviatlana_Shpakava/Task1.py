import json

names_workers = {
    "name1": "Sam",
    "name2": "Paul",
    "name3": "David",
    "name4": "Bob"
}

with open("names.json", "w") as file:
    json.dump(names_workers, file)

with open("names.json", "r") as file_:
    names = json.load(file_)
    print(names)
