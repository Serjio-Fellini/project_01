# Задача 1.1.
# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
# ___________________________________________________________________________________________________________

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
Track1 = my_favorite_songs[:14]
Track2 = my_favorite_songs[16:30]
TrackPredEnd = my_favorite_songs[my_favorite_songs.rfind('p')-10:my_favorite_songs.rfind('p')+1]
TrackEnd = my_favorite_songs[-13:]
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
# print (Track1, TrackEnd, Track2, TrackPredEnd)
print (Track1)
print (TrackEnd)
print (Track2)
print (TrackPredEnd)
