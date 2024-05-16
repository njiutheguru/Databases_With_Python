# sqlite is light in terms of setup, administration, and resources
# sqlite is serverless
# sqlite databases are local with files stored on disk
# Accessing and manipulating data is extremely quick
# sqlite is ACID-complinat
# ACID - Atomic, consistent, isolated, and durable (ACID)
# Breat database for prototyping
#

import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# createa table...
# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies 
#                (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''INSERT INTO Movies VALUES
                ("Taxi Driver", "Martin Scorsese", 1976)''')

cursor.execute('''SELECT * FROM Movies''')
print(cursor.fetchone())


connection.commit()
connection.close()





