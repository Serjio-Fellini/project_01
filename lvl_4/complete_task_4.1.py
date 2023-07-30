

# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:



#  Удалим ранее созданные таблицы Students и School, чтобы при 
#  повторном запуске кода не получать ошибок что таблицы уже созданы
#import sqlite3

#connection = sqlite3.connect('teachers.db')
#cursor = connection.cursor()
#query = 'DROP TABLE Students;'
#cursor.execute(query)
#connection.commit()
#query = 'DROP TABLE School;'
#cursor.execute(query)
#connection.commit()
#connection.close()


#  Создаём таблицу School:
import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS School (
School_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL,
Place_Count INTEGER NOT NULL);"""
cursor.execute(query)
connection.commit()
connection.close()


#  Заполняем таблицу School:

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO School (School_Id, School_Name, Place_Count)
VALUES
(1,'Протон',200),
(2,'Преспектива',300),
(3,'Спектр',400),
(4,'Содружество',500);"""
cursor.execute(query)
connection.commit()
connection.close()


#  Создаём таблицу Students:

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE IF NOT EXISTS Students (
Student_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY);"""
cursor.execute(query)
connection.commit()
connection.close()


#  Заполняем таблицу Students:

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
(201,'Иван',1),
(202,'Петр',2),
(203,'Анастасия',3),
(204,'Игорь',4);"""
cursor.execute(query)
connection.commit()
connection.close()


#  ОСНОВНАЯ ЧАСТЬ КОДА
#  Первый вариант без JOIN:

def get_connection():
  connection = sqlite3.connect("teachers.db")
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_info(Student_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * FROM Students WHERE Student_Id = ?;"
    cursor.execute(sql_query,(Student_Id,))
    records = cursor.fetchall()
    close_connection(connection)
    print("Первый вариант без JOIN:")
    for row in records:
      print ("ID Студента:", row[0])
      print ("Имя студента:", row[1])
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

def get_school_info(School_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * FROM School WHERE School_Id = ?;"
    cursor.execute(sql_query,(School_Id,))
    records = cursor.fetchall()
    close_connection(connection)
    for row in records:
      print ("ID школы:", row[0])
      print ("Название школы:", row[1], "\n")
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

get_student_info(201) #  получаем информацию о студенте
get_school_info(1) #  получаем информацию о школе


#  Второй вариант с JOIN:

def get_connection():
  connection = sqlite3.connect("teachers.db")
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_school_info(Student_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = """SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
                   FROM Students
                   JOIN School ON Students.School_Id = School.School_Id
                   WHERE Student_Id = ?;"""
    cursor.execute(sql_query, (Student_Id,))
    res = cursor.fetchone()
    close_connection(connection)
    print("Второй вариант с JOIN:")
    print ("ID Студента:", res[0])
    print ("Имя студента:", res[1])
    print ("ID школы:", res[2])
    print ("Название школы:", res[3])
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

get_student_school_info(201)
