# create and query sqlite database
# Create a users table
# Columns for user_id, First Name, Last Name, and Email Address
# Insert five records into the database
# Two records should have email addresses ending in @gmail.com
# Query the datbase to retrieve all email addresses
# Use the sqlite3 module with SQL statements or SQLAlchemy
#

##### THE SIMPLE STRAIGHT-FORWAD WAY TO GO THROUGH IT ########


import sqlite3

connection = sqlite3.connect('users_sqlite.db')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Users
          (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
          first_name TEXT, last_name TEXT, email_address TEXT)''')

users_to_insert = [('Sarah','Perry','sarah.perry@gmail.com'),
                   ('Ann','Mungai','annmungai@gmail.com'),
                   ('Jessica','Jones','jessicajones@outlook.com'),
                   ('Bruno','Collins','brunocollins@yahoo.com'),
                   ('Percy','Colton','percy_colton@yahoo.com'),
                   ('John','Doe','johndoe@gmail.com')]

c.executemany('''INSERT INTO Users(first_name, last_name, email_address) VALUES (?,?,?)''', users_to_insert)

c.execute("SELECT * FROM Users")
print(c.fetchall())

connection.commit()
connection.close()








