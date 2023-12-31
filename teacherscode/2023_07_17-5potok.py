# -*- coding: utf-8 -*-
"""17_07_2023_5potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P1OVPgn3M0Qo3oeU-eiq0E1YBNvrkMNQ
"""

# Задача 1
salary = float(input("Введи ЗП:"))
expenses = float(input("Введи расходы:"))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
exptemp = expenses
if salary >= expenses:
  print ("Входные данные не соответствуют условию задачи")
else:
  for i in month:
    print ("Сейчас месяц", i)
    if i != 1:
      all_salary = salary * i
      print ("Зарплата ", all_salary)
      expenses = expenses*1.1
      exptemp = exptemp + expenses
      print ("Расходы ", exptemp)
    else:
      print ("1 месяц без процентов")
      print ("Зарплата", salary)
      print ("Расходы", expenses)
    live = abs(all_salary - exptemp)
    print ("Сотрудник будет должен: ", round(live,2), "рублей")

# Интерполяционный поиск
import random

def intsearch(arr,x):
  low = 0
  high = len(arr)-1
  while low <= high and x >= arr[low] and x <= arr[high]:
    index =  low + int(((x-arr[low])*(high-low) // (arr[high]-arr[low])))
    if arr[index] == x:
      return index
    if arr[index] < x:
      low = index + 1
    else:
      high = index - 1
  return -1

# Тестовый массив
arr = []
for i in range(10):
  arr.append(random.randint(1,100))
arr.sort()
print (arr)
x = int(input("Введи число:"))

# Вызов функции
if intsearch(arr,x) != -1:
  print ('Элемент найден под индексом', intsearch(arr,x))
else:
  print ('Элемент не найден в массиве')

# Задача 3
import os

def get_paths(path = '.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    yield abs_path

    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths("тест1"):
  print (i)

# Задача 4
import os

def get_paths(path = '.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    if os.path.isfile(abs_path) is True:
      yield abs_path

    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)


for i in get_paths("тест1"):
  print (i)