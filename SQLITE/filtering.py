import sqlite3

connection = sqlite3.connect("Movies.db")
c = connection.cursor()
# code
release_year = (2012,)# MUST BE A TUPLE TO AVOID SQL INJECTION
c.execute("SELECT * FROM Movies WHERE year = ?", release_year)

print(c.fetchall())

connection.commit()
connection.close()