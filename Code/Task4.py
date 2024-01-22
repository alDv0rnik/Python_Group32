"""
Прочтите data.csv файл. Запишите имена колонок в отдельную переменную,
а в другую все остальные строки. Создайте список словарей, где ключами будут имена колонок,
а значениями будут строки. Выполните сериализацию данных в при помощи модуля pickle
Сохраните данные в файл dat.

Для чтения csv используйте метод reader
"""
import csv
import pickle
import json


with open('data/data.csv', "r") as file:
    data = list(csv.reader(file, delimiter=","))

col = data[0]
rows = data[1:]

names = []
for row in rows:
    names.append({col[0]: row[0], col[1]: row[1], col[2]: row[2]})

with open('names.dat', 'wb') as out_file:
    pickle.dump(names, out_file)

with open('names.json', 'w') as o_file:
    json.dump(names, o_file)


