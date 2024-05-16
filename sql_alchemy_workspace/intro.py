import sqlalchemy

# The name of the database needs to be in the same folder as the program running and besides that the string "sqlite:///{name}" has to be passed before.
engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
    for row in result:
        print(row)
