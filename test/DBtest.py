import pymysql

my_db = pymysql.connect(
    host="reunion.mysql.database.azure.com",
    port=3306,
    user="trmb",
    port =3306,
    password="$$BASMOTESH123",
    database ='reunion'
) 

my_cursor = my_db.cursor()

my_cursor.execute("SHOW TABLES")
for db in my_cursor:
    print(db)

