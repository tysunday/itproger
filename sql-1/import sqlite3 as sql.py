import sqlite3 as sql

#Создание и подключение к БД
connection = sql.connect('test.sqlite')
#Cоздание курсора для работы с БД
q = connection.cursor() 

# q.execute('''CREATE TABLE user (id int auto_increment primary key, name varchar, password varchar)''')
# connection.commit()

user_name = input("Input you name: ")
user_password = input("Input password: ")

print("List of users: \n")
q.execute("INSERT INTO user (name, password) VALUES('%s', '%s')"%(user_name, user_password))
connection.commit()

q.execute("SELECT * FROM user") 
row = q.fetchone()

while row is not None:
    print("Name: ", row[1], "| Password:", row[2])
    row = q.fetchone()

# Отключение от базы данных
q.close()
connection.close()