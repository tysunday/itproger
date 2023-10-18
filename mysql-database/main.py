import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="python-example"
)

myCur = mydb.cursor()

# sql = "CREATE DATABASE `python-example`"
# sql = "SHOW DATABASES"
# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))"
# sql="SHOW TABLES"
sql = "INSERT INTO articles (title, intro, date) VALUES(%s, %s, %s)"
articles = [
        (
        'Первая статья',
        'Hello text',
        '2020-12-55'
    ),
    (
        'Третья статья',
        'Hello text',
        '2020-12-09'
    ),
    (
        'Четвёртая статья',
        'Hello text',
        '2020-08-12'
    ),
]

myCur.executemany(sql,articles)
mydb.commit()