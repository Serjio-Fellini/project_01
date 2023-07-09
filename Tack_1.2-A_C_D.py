# Задача 1.2.
# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
#my_favorite_songs = [
#    ['Waste a Moment', 3.03],
#    ['New Salvation', 4.02],
#    ['Staying\' Alive', 3.40],
#    ['Out of Touch', 3.03],
#    ['A Sorta Fairytale', 5.28],
#    ['Easy', 4.15],
#    ['Beautiful Day', 4.04],
#    ['Nowhere to Run', 2.58],
#    ['In This World', 4.02],
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
#___________________________________________________________________________________________________________

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# Вычисляем количество песен в списке
Tracks= len(my_favorite_songs)
# Проверка промежуточных результатов при отладке
#print(Tracks)

import random
# В списке rand_list формируем список номеров случайно выбранных песен
rand_list=[]
# Количество случайно выбираемых песен равно 3
n=3
for i in range(n):
    # Первый номер прописываем без проверки условия на уникальность
    randomiser=random.randint(0,Tracks-1)
    if i == 0:
        rand_list.append(randomiser)
    else:
        # Для последующих номеров проверяем уникальность,
        # и в случае неуникальности генерируем номер заново
        flajok1=1
        while flajok1 > 0:
            flajok1=0
            randomiser=random.randint(0,Tracks-1)
            for j in range(i):
                if rand_list[j] == randomiser:
                    flajok1=1
        rand_list.append(randomiser)
    # Проверка промежуточных результатов при отладке
    #print("i =", i)
# Cписок номеров случайно выбранных песен сформирован
# Проверка промежуточных результатов при отладке
#print(rand_list)
alltime_min=0
alltime_sec=0
for i in range(n):
#    Проверка промежуточных результатов при отладке
#    print (my_favorite_songs [int(rand_list[i])])
#    print(int(my_favorite_songs [int(rand_list[i])][1]))
#    print((my_favorite_songs [int(rand_list[i])][1])%1)
#    print(round(((my_favorite_songs [int(rand_list[i])][1])%1),2))
# Из каждой песни сумируем минуты
    alltime_min=alltime_min+int(my_favorite_songs [int(rand_list[i])][1])
# Из каждой песни суммируем секунды
    alltime_sec=alltime_sec+round(((my_favorite_songs [int(rand_list[i])][1])%1),2)
# Проверка промежуточных результатов при отладке
#print(alltime_min)
#print(alltime_sec)
if alltime_sec >= 0.6:
# Выделяем из секунд, превышающих 60, дополнительные минуты
    alltime_min=alltime_min+int(alltime_sec/0.6)
    alltime_sec=alltime_sec-(0.6*int(alltime_sec/0.6))
# Округляем оставшиеся секунды до 2 знаков
alltime_sec=round(alltime_sec,2)
# Проверка промежуточных результатов при отладке
#print(alltime_min)
#print(alltime_sec)
alltime=alltime_min+alltime_sec
# Используем форматный вывод ["%.2f" %] для гарантированной индикации двух знаков после запятой
print("Три песни звучат","%.2f" % alltime,"минут.")

# Переводим минуты и секунды в формат времени
import datetime
timeobj= datetime.time(00,alltime_min,int(alltime_sec*100))
print("Три песни звучат", timeobj.strftime("%M:%S"),"минут.")
