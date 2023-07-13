# Задача 1.3.
# Напишите скрипт, который принимает от пользователя номер месяца,
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
    #______________________________________________________________________________________________
# Подключаем библиотеки datetime и locale с локализацией 'ru'

import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru')
# Запрашиваем ввод месяца и переводим полученное в формат целого числа
print("Введите номер месяца:")
num_mes=input()
num_mes=int(num_mes)
# Проверяем принадлежность введенного числа допустимому диапазону
if num_mes<1:
    print("Такого месяца нет!")
elif num_mes>12:
    print("Такого месяца нет!")
else:
    # Если диавазон допустим, формируем с полученным месяцем дату 1 числа 0001 года
    name_mes=datetime.date(1, num_mes, 1)
    # Вычисляем дату 1 числа следующего месяца
    if num_mes == 12:
        next_mes=datetime.date(2, 1, 1)
    else:
        next_mes=datetime.date(1, num_mes+1, 1)
    # Вычисляем дельту между первыми числами введенного месяца и следующего месяца
    timedelta=next_mes-name_mes
    # Выделяем из получившейся дельты количество дней
    timedelta=str(timedelta)[:2]
    # Группируем результат и выводим на печать
    print("Вы ввели", name_mes.strftime("%B"), timedelta, "дней")