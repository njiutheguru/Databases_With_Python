# uses sql alchemy WITH expressions!!!
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///user_db_db.db', echo=True)
## The data has to be in a list in dictionary format with the key being the column name. 

users_to_insert = [{'first_name':'Sarah','last_name':'Perry','email_address':'sarah.perry@gmail.com'},
                   {'first_name':'Ann','last_name':'Mungai','email_address':'annmungai@gmail.com'},
                   {'first_name':'Jessica','last_name':'Jones','email_address':'jessicajones@outlook.com'},
                   {'first_name':'Bruno','last_name':'Collins','email_address':'brunocollins@yahoo.com'},
                   {'first_name':'Percy','last_name':'Colton','email_address':'percy_colton@yahoo.com'},
                   {'first_name':'John','last_name':'Doe','email_address':'johndoe@gmail.com'}]




metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table('Users', metadata,
                               sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True),
                               sqlalchemy.Column('first_name', sqlalchemy.String),
                               sqlalchemy.Column('last_name', sqlalchemy.String),
                               sqlalchemy.Column('email_address', sqlalchemy.String),
                               
                               )


metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)

    conn.close()

    
