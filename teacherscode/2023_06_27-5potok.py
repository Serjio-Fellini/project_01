# -*- coding: utf-8 -*-
"""27_06_2023_5potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K1ri1RuAZEAJaej1V_UUMB2hkxbdrPgl
"""

# Алгоритм Евклида делением
a = 35
b = 14
n = 0
while a != 0 and b != 0:
  n += 1
  print ("Сейчас итерация: ", n)
  if a > b:
    a = a % b
    print (a)
  else:
    b = b % a
    print (b)
print ("Итог", a + b)

# Алгоритм Евклида вычитанием
a = 35
b = 14

while a != b:
  print ("Значение a", a)
  print ("Значение b", b)
  if a > b:
    a = a - b
  else:
    b = b - a

print (b)

a = int(input("Введи делимое:"))
b = int(input("Введи делитель:"))

try:
  x = a/b
  print ("Результат", x)
except ZeroDivisionError:
  print ("У вас деление на 0")
finally:
  print ("Отработал блок файнали")
  a = int(input("Введи делимое:"))
  b = int(input("Введи делитель:"))
  x = a/b
  print ("Результат", x)

import random
x = [1,2,3,4,6,7.08,6.66,'test1','test2']
print (random.choice(x))

import random

#x = random.random()
#print (x)

y = random.uniform(1.5,5.5)
print (round(y,3))