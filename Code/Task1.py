"""
Считайте элементы списка names и запишите их в  файл names.txt в формате
1) <Name>
2) <Name>
...

names = ['Richard', 'Din Esh', 'Erlich', 'Bighead']
"""
names = ['Richard', 'Din Esh', 'Erlich', 'Bighead']


def write_names(list_names: list) -> None:
    with open("names.txt", "w") as file:
        for i, name in enumerate(list_names, start=1):
            file.write(f"{i} - {name}" + "\n")


write_names(names)