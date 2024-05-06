import pymysql
from datetime import datetime, timezone

# Establishing a connection to the database
try:
    my_db = pymysql.connect(
    host="reunion.mysql.database.azure.com",
    user="trmb",
    password="$$BASMOTESH123",
    database = 'reunion'    
    )
except:
    print("error in connection")
    
# Creating a cursor object to interact with the database
my_cursor = my_db.cursor()

# Defining the SQL INSERT statement
sql1 = "INSERT INTO FamilyFollowing (FollowingFamilyId, FollowedFamilyId) VALUES (1, 5)"
sql2 = "INSERT INTO FamilyFollowing (FollowingFamilyId, FollowedFamilyId) VALUES (1, 3)"
query = "SELECT * FROM User"

try:
    # Executing the SQL statement
    #my_cursor.execute(sql, data)
    #my_cursor.execute(sql1)
    #my_cursor.execute(sql2)
    my_cursor.execute(query)
    rows = my_cursor.fetchall()
    for row in rows:
        print(row)
    # Committing the changes
    my_db.commit()

    print("Data inserted successfully. Inserted ID:", my_cursor.lastrowid)

except pymysql.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Closing the cursor and database connection
    if my_cursor:
        my_cursor.close()
    if my_db:
        my_db.close()
