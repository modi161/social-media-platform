import pymysql
from datetime import date

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
sql = "INSERT INTO user (username, FirstName, email, password_hash, lastname, Gender, Birthdate, FamilyID, FamilyRole ,bio ,photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


# Example data to insert
# Note: Modify the values accordingly. Ensure dates and other types are correctly formatted.
data = (
    "Alaa",          # username
    "boody",             # FirstName
    "Alaa.rashad@teeztarek.com",  # email
    "1234",    # password_hash
    "tezzztarek",              # lastname

    True,               # Gender (True for male, False for female)
    date(2003, 8, 14),   # Birthdate
    6,                  # FamilyID (assumes a valid ID from the 'family' table)
    False,                # FamilyRole (True for admin, False for normal member)
    "I Am Tarek Shalaby data science engineer",
    "https://www.newarab.com/sites/default/files/2023-08/GettyImages-1258930731.jpg"
)

try:
    # Executing the SQL statement
    my_cursor.execute(sql, data)

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
