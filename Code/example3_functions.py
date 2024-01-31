import sqlite3


def to_uppercase(id_: int, raw_text: str) -> str:
    return f"{id_+1} -> {raw_text.upper()}"


with sqlite3.connect(':memory:') as connection:
    connection.create_function('upper', 2, to_uppercase)

    connection.execute(
        "CREATE TABLE users(id INTEGER, name VARCHAR(20))"
    )
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users(id, name) VALUES (1, 'John'), (2, 'Mike')"
    )
    lines = cursor.execute(
        "SELECT id, upper(id, name) FROM users"
    ).fetchall()
    print(lines)
