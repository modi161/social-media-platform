import pymysql
from datetime import datetime

# Establishing a connection to the database
try:
    my_db = pymysql.connect(
        host="reunion.mysql.database.azure.com",
        user="trmb",
        password="$$BASMOTESH123",
        database='reunion'
    )
except Exception as e:
    print("Error in connection:", e)

# Creating a cursor object to interact with the database
my_cursor = my_db.cursor()

# Defining the SQL INSERT statement for the 'user' table
sql = "INSERT INTO Content (description, timestamp, visibility, Type, userId) VALUES (%s, %s, %s, %s, %s)"
sql2 = "INSERT INTO ContentPhotos (contentId, photoUrl) VALUES (%s, %s)"

# Example data to insert
# Note: Modify the values accordingly. Ensure dates and other types are correctly formatted.
data = (
    "ba7eb Rashad",   
    datetime.now(),          
    1,  
    1,  
    6,  
)

data2 = (
    6,
    "https://prod-media.beinsports.com/image/1706000402182_8554071a-cf34-4e7c-baeb-f0f8555cb5f8.jpg?ver=06-02-2024"
)

try:
    # Executing the SQL statement
    #my_cursor.execute(sql, data)
    my_cursor.execute(sql2, data2)
    # Committing the changes
    my_db.commit()

    print("User data inserted successfully. Inserted ID:", my_cursor.lastrowid)

except pymysql.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Closing the cursor and database connection
    if my_cursor:
        my_cursor.close()
    if my_db:
        my_db.close()
