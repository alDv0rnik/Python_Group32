import json
import sqlite3


def to_string(data):
    return json.dumps(data)


def to_json(raw_data):
    return json.loads(raw_data)


with sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES) as connection:
    # Регистрируем функцию-адаптер
    sqlite3.register_adapter(dict, json.dumps)
    connection.execute("CREATE TABLE test(n json)")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO test(n) VALUES(?)", ({'a': 1, 'foo': 2, 'bar': 3},))
    line = cursor.execute('SELECT * FROM test').fetchone()
    print(line)
    print(type(line[0]))

    # Регистрируем функцию-конвертер
    sqlite3.register_converter('json', to_json)
    cursor.execute("SELECT * FROM test")
    line_ = cursor.fetchone()
    print(line_)
    print(type(line_[0]))