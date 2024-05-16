import sqlite3
conn = sqlite3. connect("friends.db")
# curso object
c = conn.cursor()

people = [
    ("Roald", "Amundsen",5),
    ("Mark", "Hilda",7),
    ("Jimmy", "Bruno",8),
    ("Henry","Mark",11),
    ("Daniel","Bjarne",12)

]

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

############ Dynamic insertions
average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print(f"NOW INSERTING {person} data............")
    average += person[2]
print(average/len(people))


conn.commit()
conn.close()



















