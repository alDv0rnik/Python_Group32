import sqlite3

connection = sqlite3.connect("movies.sqlite3")
cursor = connection.cursor()

# connection.execute(
#     "CREATE TABLE movies ("
#     "id INTEGER,"
#     " title VARCHAR(50),"
#     " year INTEGER,"
#     " director VARCHAR(20)"
#     ")"
# )
#
# connection.execute(
#     "INSERT INTO movies(id, title, year, director)"
#     "VALUES (1, 'Star Wars. Ep.4', 1979, 'Lucas')"
# )
# connection.execute(
#     "INSERT INTO movies(id, title, year, director)"
#     "VALUES (2, 'Alien', 1982, 'Scott'),"
#     "(3, 'Terminator', 1985, 'Cameron')"
# )

# cursor.execute("DELETE FROM movies WHERE id IN (2, 3)")
year = 1980
id_ = 1

# cursor.execute("UPDATE movies SET year=? WHERE id=?", (year, id_))

movies = cursor.execute(
    "SELECT * FROM movies"
).fetchall()
# print(type(movies))
print(movies)

connection.commit()
cursor.close()