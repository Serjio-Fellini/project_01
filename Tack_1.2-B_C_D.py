# Задача 1.2.
# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
#my_favorite_songs_dict = {
#    'Waste a Moment': 3.03,
#   'New Salvation': 4.02,
#   'Staying\' Alive': 3.40,
#   'Out of Touch': 3.03,
#   'A Sorta Fairytale': 5.28,
#   'Easy': 4.15,
#   'Beautiful Day': 4.04,
#   'Nowhere to Run': 2.58,
#   'In This World': 4.02,
#}
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
#___________________________________________________________________________________________

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Вычисляем количество песен в списке
Tracks=len (my_favorite_songs_dict)
# Проверка промежуточных результатов при отладке
#print(Tracks)
# Количество случайно выбираемых песен равно 3
n=3
# В списке rand_list формируем список номеров случайно выбранных песен
rand_list=[]
import random
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
alltime_min=0
alltime_sec=0
# Проверка промежуточных результатов при отладке
#print(rand_list)
j=0
# Производим перебор ключей cловаря, и если его порядковый номер имеется в списке
# случайно выбранных, считываем запись, содержащую длительность звучания песни
for key_in in my_favorite_songs_dict.keys():
    if j in rand_list:
        # Проверка промежуточных результатов при отладке
        #print(j, "  ",key_in)
        alltime=my_favorite_songs_dict[key_in]
        # Проверка промежуточных результатов при отладке
        #print(alltime)
        # Из каждой песни сумируем минуты
        alltime_min=alltime_min+int(alltime)
        # Из каждой песни суммируем секунды
        alltime_sec=alltime_sec+round(((alltime)%1),2)
        j=j+1
    else:
        j=j+1
# Проверка промежуточных результатов при отладке
# print(alltime_min)
# print(alltime_sec)



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
