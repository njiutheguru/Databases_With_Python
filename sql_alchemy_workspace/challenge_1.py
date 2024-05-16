# uses sql alchemy without expressions!!!
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///user_db.db', echo=True)
users_to_insert = [{'first_name':'Sarah','last_name':'Perry','email_address':'sarah.perry@gmail.com'},
                   {'first_name':'Ann','last_name':'Mungai','email_address':'annmungai@gmail.com'},
                   {'first_name':'Jessica','last_name':'Jones','email_address':'jessicajones@outlook.com'},
                   {'first_name':'Bruno','last_name':'Collins','email_address':'brunocollins@yahoo.com'},
                   {'first_name':'Percy','last_name':'Colton','email_address':'percy_colton@yahoo.com'},
                   {'first_name':'John','last_name':'Doe','email_address':'johndoe@gmail.com'}]


with engine.connect() as conn:
    conn.execute(sqlalchemy.text('''CREATE TABLE IF NOT EXISTS Users (user_id INTEGER primary key autoincrement, first_name text, last_name text, email_address text)'''))

    conn.execute(sqlalchemy.text('''INSERT INTO Users (first_name, last_name, email_address) VALUES (:first_name, :last_name, :email_address)'''), users_to_insert)

    result = conn.execute(sqlalchemy.text('''SELECT * FROM Users'''))
    for row in result:
        print(row)

    conn.close()



