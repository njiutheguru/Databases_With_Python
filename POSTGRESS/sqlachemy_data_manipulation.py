from sqlalchemy import create_engine, select
from sqlalchemy import Table, column, Integer, Float, String, MetaData


engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433/red30', echo=True)
metadata = MetaData()
sales_table = Table('sales', metadata, autoload_with=engine)
metadata.create_all(engine)

with engine.connect() as conn:
    # read
    for row in conn.execute(select(sales_table)):
        print(row)
    # create
    # CRUD == CREATE, READ, UPDATE AND DELETE OPERATIONS
    insert_statemnt = sales_table.insert().values(order_num = 1105910,
                                                  cust_name='Syman Mapstone',
                                                  prod_number = 'EB521',
                                                  prod_name = 'Understanding Black Box Algorithms',
                                                  quantity=3,
                                                  price=19.5,
                                                  discount=0,
                                                  order_total=58.5)

    conn.execute(insert_statemnt)

    # update statement
    update_statement = sales_table.update().where(sales_table.c.order_num == 1105910).values(quantity=2, order_total=39)
    conn.execute(update_statement)
    # confirm update
    reselect_statement = sales_table.select().where(sales_table.c.order_num==1105910)
    updated_sale = conn.execute(reselect_statement).first()
    print(updated_sale)
    # delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num == 1105910)
    conn.execute(delete_statement)
    # confirm delete
    not_found = conn.execute(reselect_statement)
    print(not_found.rowcount)
