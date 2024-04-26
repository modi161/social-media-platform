import pymysql

my_db = pymysql.connect(
    host="localhost",
    user="root",
    password="Tarek-1488@ZC"
) 

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE SMP")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

