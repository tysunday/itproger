import sqlite3 as sql

# Подключение к базе данных.
connection = sql.connect('test.sqlite')
# Создание курсора для работы с БД
q = connection.cursor()

q.execute('''CREATE TABLE user (id int auto_increment primary key, name varchar, password varchar) ''')
connection.commit()

name = input("Введите ваш имя: ")
password = input("Введите пароль: ")

print

# Отключение от базы данных
q.close()
connection.close()
