"""
Считайте элементы списка names и запишите их в  файл names.txt в формате Position) Name

names = ['Richard', 'Din Esh', 'Erlich', 'Bighead']
"""
names = ['Richard', 'Din Esh', 'Erlich', 'Bighead']

with open('names.txt', 'w') as file:
    for i, name in enumerate(names, start=1):
        file.write(f"{i}) {name}\n")