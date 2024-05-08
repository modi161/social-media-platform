import pymysql

my_db = pymysql.connect(
    host="reunion.mysql.database.azure.com",
    port=3306,
    user="trmb",
    password="$$BASMOTESH123",
    database ='reunion'
) 

my_cursor = my_db.cursor()

# my_cursor.execute("SHOW TABLES")

#my_cursor.execute(f'UPDATE Family SET profilephoto = "https://www.aupair.com/summaryBoxImages/au-pair-wiki-photos-2632.jpg", coverphoto = "https://images.pexels.com/photos/39691/family-pier-man-woman-39691.jpeg" WHERE id = {5};')
#my_db.commit()



my_cursor.execute("Select * from contentphotos")




for db in my_cursor:
    print(db)