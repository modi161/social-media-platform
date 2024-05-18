import pymysql

my_db = pymysql.connect(
    host="reunion.mysql.database.azure.com",
    port=3306,
    user="trmb",
    password="$$BASMOTESH123",
    database ='reunion'
) 

my_cursor = my_db.cursor()



my_cursor.execute("Select * from userlikedcontent")
# my_cursor.execute("Select * from ")




for db in my_cursor:
    print(db)