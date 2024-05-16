import sqlalchemy

# The name of the database needs to be in the same folder as the program running and besides that the string "sqlite:///{name}" has to be passed before.
engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

metadata = sqlalchemy.MetaData()

movies_table = sqlalchemy.Table("Movies",metadata,
                                sqlalchemy.Column("title", sqlalchemy.Text),
                                sqlalchemy.Column("director", sqlalchemy.Text),
                                sqlalchemy.Column("year", sqlalchemy.Integer),
                                )

metadata.create_all(engine)

with engine.connect() as conn:
    for row in conn.execute(sqlalchemy.select(movies_table)):
        print(row)
        
