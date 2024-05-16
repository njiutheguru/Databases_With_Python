  # create a database my_sql
# insert and query data
# data will represent a tech company's online sales
# columns: order_num, oder_type, cust_name, prod_category, prod_number, prod_name, quantity, price, discount, and order total

 ##########################3
# 1. Create a database named Red30
# 2. Create a table called sales
# 3. Insert five rows, where order_num is the primary key.
# 4. Query for the most expensive order
# 5. Discover who ordered the most expensive order.


from sqlalchemy import Column, String, Integer, Numeric, create_engine, select, func
from sqlalchemy.orm import registry, Session


password = input("Enter you MYSQL password:")

engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/red31',echo=True)

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Sale(Base):
    __tablename__ = 'sales'

    order_num = Column(Integer, primary_key=True)
    cust_name = Column(String)
    prod_name = Column(String)
    prod_number = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    discount = Column(Integer)
    order_total = Column(Integer)

    def __repr__(self):
        return "<Sale(order_num = '{0}', cust_name = '{1}', prod_name='{2}', quantity='{3}',price='{4}',discount='{5}',order_total='{6}')"
    

Base.metadata.create_all(engine)

with Session(engine, future=True) as session:
    sale_1 = Sale(cust_name="Spencer Educators", prod_number="DK87U",prod_name="Byod driver", quantity=2, price=99,discount=2, order_total=178)
    sale_2 = Sale(cust_name="John Mac", prod_number="HTMLGIX",prod_name="Expensive Lux", quantity=8, price=979,discount=1, order_total=18)
    sale_3 = Sale(cust_name="Joe Michael", prod_number="HTX7U",prod_name="Hand Dryer", quantity=10, price=39,discount=2, order_total=17)
    sale_4 = Sale(cust_name="Stephen Njiu", prod_number="STNTC",prod_name="Alpha Algo", quantity=2, price=100,discount=1, order_total=100)
    sale_5 = Sale(cust_name="Hilay Odhiambo", prod_number="HODIMS",prod_name="Gymanistics", quantity=5, price=339,discount=1, order_total=8)

    sales = [sale_1, sale_2, sale_3, sale_4, sale_5]

    session.bulk_save_objects(sales)

    session.flush()
    session.close()

    ## querying
    max_query = select(func.max(Sale.order_total))
    max_order = session.execute(max_query).scalar()
    print(max_order)

    results_query = select(Sale).order_by(Sale.order_total.desc())
    results_in_order = session.execute(results_query)
    for order in results_in_order:
        print(order)










