import sqlite3
conn = sqlite3.connect("friends.db")
# create a cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")

# insert_query = '''INSERT INTO friends
#                     VALUES ('Merriwether', 'Lewis', 7)'''
# c.execute(insert_query)
# Dynamic insertions...
data = ("Steve", "Bruno", 4) # the data has to match the tables header...
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)


# commit changes
conn.commit()
conn.close()












