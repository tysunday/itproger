import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="python-example"
)

myCur = mydb.cursor()

# sql = "SELECT id, date FROM articles WHERE title NOT LIKE %s AND id = %s ORDER BY title DESC"
# myCur.execute(sql, ('%первая%', 13))

# sql = "SELECT id, date FROM articles LIMIT 1 OFFSET 2"
# myCur.execute(sql)

# res = myCur.fetchall()
# print(res)
# for el in res:
#     print(el)

# sql = "UPDATE articles SET title = %s WHERE id = %s"
# myCur.execute(sql,("Updated text", 3))
# mydb.commit()

# sql = "DELETE FROM articles WHERE title = %s"
# myCur.execute(sql,('Updated text',))
# mydb.commit()

# sql = "DELETE FROM articles" # delete all data in table.
sql = "DROP TABLE articles"
myCur.execute(sql)
mydb.commit()