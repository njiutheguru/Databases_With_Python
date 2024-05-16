import sqlite3

connection = sqlite3.connect("Movies.db")
c = connection.cursor()
famous_films = [("Pulp Fiction", "Quentin Tarantino", 1994),
                ("Back To The Future", "Robert Zemeckis", 1985),
                ("Moonrise Kingdom", "Wes Anderson", 2012)]

c.executemany('INSERT INTO  Movies VALUES (?,?,?)', famous_films)

c.execute('SELECT * FROM Movies')

print(c.fetchall())

connection.commit()
connection.close()