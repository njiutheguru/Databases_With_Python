from sqlalchemy import create_engine, select
from sqlalchemy import Table, column, Integer, Float, String, MetaData
from sqlalchemy.ext.automap import automap_base

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433/red30', echo=True)

Base = automap_base()
Base.prepare(autoload_with=engine)
Sales = Base.classes.sales


