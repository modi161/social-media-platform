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
sql = "INSERT INTO family (familyname, bio, creationdate , coverphoto ,profilephoto) VALUES (%s, %s, %s, %s, %s)"

# Example data to insert
data = ("mexico", "This is the mexico family.", datetime.now(timezone.utc),"https://www.newarab.com/sites/default/files/2023-08/GettyImages-1258930731.jpg","https://www.newarab.com/sites/default/files/2023-08/GettyImages-1258930731.jpg")

try:
    # Executing the SQL statement
    my_cursor.execute(sql, data)

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
