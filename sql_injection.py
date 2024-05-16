import sqlite3
conn = sqlite3.connect("users.db")
u = input("Please Enter your username: ...")
p = input("Please Enter your password:....")


c = conn.cursor()
# insert the data into the tables first...
# people = [
#     ("Roald", "Amundf009idsen"),
#     ("Mark", "Hijjj9lda"),
#     ("Jimmy", "dfdfd990runo"),
#     ("Henry","kkdfdf9dfd"),
#     ("Daniel","Bjarne")

# ]

# c.executemany("INSERT INTO password_management VALUES (?,?)", people)


# bypass password in sql ==> [' OR 1=1 --]
# query = f"SELECT * FROM  password_management WHERE username ='{u}' AND password='{p}'"
query = f"SELECT * FROM  password_management WHERE username =? AND password= ?"
c.execute(query, (u,p))# resistant to sql injection...
result = c.fetchone()
if result:
    print("welcome back...")
else:
    print("Failed Login")

conn.commit()
conn.close()