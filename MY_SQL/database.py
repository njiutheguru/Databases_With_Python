import mysql.connector as mysql

def connect(db_name):
    try:
        password = input("Enter your MYSQL password:")
        return mysql.connect(host='localhost',
                   user='root',
                   password =password,
                   database = db_name)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    db = connect("Projects")
    cursor = db.cursor()
    # querying all the database...
    cursor.execute("SELECT * FROM Projects")
    project_records = cursor.fetchall()
    print(project_records)

    db.close()