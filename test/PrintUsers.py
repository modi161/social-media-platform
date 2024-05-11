import pymysql

try:
    # Establishing a connection to the database
    my_db = pymysql.connect(
        host="reunion.mysql.database.azure.com",
        user="trmb",
        password="$$BASMOTESH123",
        database='reunion'
    )

    # Creating a cursor object to interact with the database
    my_cursor = my_db.cursor()

    # Defining the SQL SELECT statement to fetch all users
    sql = "SELECT * FROM user"

    # Executing the SQL statement
    my_cursor.execute(sql)

    # Fetching all rows from the result set
    users = my_cursor.fetchall()

    # Printing the users
    if users:
        print("All users in the user table:")
        for user in users:
            print(user)
    else:
        print("No users found in the user table.")

except pymysql.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Closing the cursor and database connection
    if my_cursor:
        my_cursor.close()
    if my_db:
        my_db.close()
