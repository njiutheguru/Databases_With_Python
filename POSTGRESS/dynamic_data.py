# postgres is highle extensibel and starndards compliant and adheres more closeley to sql standards
# Define the password of postgresql as a user input

import psycopg2


def insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount

    sale_data = {
        'order_num': order_num,
        'cust_name': cust_name,
        'prod_number': prod_number,
        'prod_name': prod_name,
        'quantity': quantity,
        'price': price,
        'discount': discount,
        'order_total': order_total
    }

    cur.execute('''INSERT INTO SALES VALUES (%(order_num)s,
    %(cust_name)s,
    %(prod_number)s,
    %(prod_name)s,
    %(quantity)s,
    %(price)s,
    %(discount)s,
    %(order_total)s)''', sale_data)


if __name__ == "__main__":
    password = input("Enter your POSTgreSQL password:")
    conn = psycopg2.connect(database="red30",
                            user="postgres",
                            password=password,
                            host="localhost",
                            port="5433")

    cursor = conn.cursor()
    ## code here
    order_num = int(input("What is the order number?\n"))
    cust_name = input("What is the customer's name? \n")
    prod_number = input("What is the product number? \n")
    prod_name = input("What ist he product name?\n")
    quantity = float(input("What is the quantity? \n"))
    price = float(input("What is the price of the product? \n"))
    discount = float(input("What is the discount, if there is one? \n"))

    print("Inputting sale data: \n")
    insert_sale(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)




    conn.commit()
    conn.close()

# sales = [(3446543, "Spencer Educators", "DK204", "BYOD-300", 2, 89, 0, 178),
#         (877334, "Karl Jones", "HTMLd", "JHM-300", 2, 39, 2, 138),
#         (955634, "Hilton Marxs", "ZMD899", "JJK900", 3, 23, 3, 89),
#         (35 2446, "Master-guru", "NNB45", "IUJ97TY6", 4, 45, 2, 233),
#         (9877658, "RAMEO", "KKOJ889J", "TTF55466F", 5, 78, 1, 23),
#         (9011221, "HDSQL", "GHTRT56", "HJ7786J", 26, 34, 1, 45)]

# cursor.executemany("INSERT INTO SALES VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)
# print("Connected to the database successfully...")
