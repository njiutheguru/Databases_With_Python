from sqlalchemy import create_engine
from sqlalchemy import Table, column, Integer, Float, String, MetaData


engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433/red30', echo=True)
metadata = MetaData()
sales_table = Table('sales', metadata, autoload_with=engine)
metadata.create_all(engine)






