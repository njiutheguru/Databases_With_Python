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


def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute('''INSERT INTO Projects (title, description) VALUES (%s, %s)''', project_data)

    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)

    cursor.executemany('''INSERT INTO Tasks (project_id, description) VALUES (%s, %s)''', tasks_data)


if __name__ == '__main__':
    db = connect("Projects")
    cursor = db.cursor()

    tasks = ["Clean Bathroom", "Clean Kitchen", "Clean Living room"]
    add_project(cursor, "Clean House", "Clean House by room", tasks)
    db.commit()

    # querying all the database...
    cursor.execute("SELECT * FROM Projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM Tasks")
    task_records = cursor.fetchall()
    print(task_records)

    db.close() 