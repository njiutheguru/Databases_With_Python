# postgres is highle extensibel and starndards compliant and adheres more closeley to sql standards
# Define the password of postgresql as a user input

import psycopg2

password = input("Enter your POSTgreSQL password:")

conn = psycopg2.connect(database="red30",
                        user="postgres",
                        password=password,
                        host="localhost",
                        port="5433")

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE SALES (ORDER_NUM INT PRIMARY KEY,
#             CUST_NAME TEXT,
#             PROD_NUMBER TEXT,
#             PROD_NAME TEXT,
#             QUANTITY INT,
#             PRICE REAL,
#             DISCOUNT REAL,
#             ORDER_TOTAL REAL);''')

# Create sales data
sales = [(3446543, "Spencer Educators", "DK204", "BYOD-300", 2, 89, 0, 178),
        (877334, "Karl Jones", "HTMLd", "JHM-300", 2, 39, 2, 138),
        (955634, "Hilton Marxs", "ZMD899", "JJK900", 3, 23, 3, 89),
        (352446, "Master-guru", "NNB45", "IUJ97TY6", 4, 45, 2, 233),
        (9877658, "RAMEO", "KKOJ889J", "TTF55466F", 5, 78, 1, 23),
        (9011221, "HDSQL", "GHTRT56", "HJ7786J", 26, 34, 1, 45)]

cursor.executemany("INSERT INTO SALES VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)

conn.commit()
conn.close()
# print("Connected to the database successfully...")


