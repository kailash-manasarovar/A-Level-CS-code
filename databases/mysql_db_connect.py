def get_users():
    import mysql.connector

    db_connection = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='patterns')

    cursor = db_connection.cursor()

    users = []

    cursor.execute("""SELECT * FROM people""")

    for row in cursor:
        user = {
            'id': row[0],
            'firstname': row[1],
            'surname': row[2],
            'password': row[3]
        }
        users.append(user)
    cursor.close()
    return users


users = get_users()
print(users)


