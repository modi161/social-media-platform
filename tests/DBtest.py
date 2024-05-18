import pymysql

my_db = pymysql.connect(
    host="reunion.mysql.database.azure.com",
    port=3306,
    user="trmb",
    password="$$BASMOTESH123",
    database ='reunion'
) 

my_cursor = my_db.cursor()



# my_cursor.execute("Delete from FamilyPendingRequests")
# my_cursor.execute("Delete from FamilyFollowing")
# my_cursor.execute("Delete from UserLikedContent")
# my_cursor.execute("Delete from ContentPhotos")
# my_cursor.execute("Drop Table content")
# my_cursor.execute("Drop Table User")
# my_cursor.execute("Delete from Family")
# my_cursor.execute("Drop Table Family")


my_cursor.execute("Show Tables")




for db in my_cursor:
    print(db)