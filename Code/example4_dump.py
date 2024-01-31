import sqlite3

with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE users(id INTEGER, name VARCHAR(20))"
    )
    cursor.execute(
        "INSERT INTO users(id, name) VALUES (1, 'John'), (2, 'Mike')"
    )
    connection.commit()

    cursor.execute("INSERT INTO users(id, name) VALUES (3, 'Alex')")
    rows = cursor.execute("SELECT * FROM users").fetchall()
    print(rows)
    connection.rollback()
    rows_ = cursor.execute("SELECT * FROM users").fetchall()
    print(rows_)

with open('dump.sql', 'w') as file:
    for line in connection.iterdump():
        file.write('%s\n' % line)
        # print('{}'.format(line))