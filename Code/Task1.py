"""
Создайте таблицу «материалы» из следующих полей: идентификатор, вес, высота
и доп. характеристики материала. Поле доп. характеристики материала должно хранить в себе
массив,  каждый  элемент  которого  является  словарем, где ключ –  название
характеристики, а значение – её определение.
"""
import sqlite3
import json


with sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES) as connection:
    connection.execute(
        "CREATE TABLE materials("
        "id INTEGER,"
        "weight DECIMAL(5, 2),"
        "height DECIMAL (5,2),"
        "extra json)"
    )
    cursor = connection.cursor()
    sqlite3.register_adapter(dict, json.dumps)
    cursor.execute(
        "INSERT INTO materials(id, weight, height, extra)"
        "VALUES (1, 35.0, 20, ?)",
        ({'a': 12, 'b': 15},)
    )
    row = cursor.execute("SELECT * FROM materials").fetchone()
    print(row)
