import sqlite3
conn = sqlite3.connect("friends.db")
c = conn.cursor()
c.execute("SELECT * FROM friends WHERE closeness > 5")
# iterate over teh cursor
# for result in c:
#     print(result)

# fetch one result
print(c.fetchone())
# fetch all results
print(sorted(c.fetchall())) # selects from second
# commit changes
conn.commit()
conn.close()