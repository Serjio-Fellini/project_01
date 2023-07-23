# ############################ОПЕРАТОРЫ############################

# TODO - условный оператор if
# TODO - операторы цикла for и while
# TODO - отладчик

# Ветвление if
# x = int(input("Введи число: "))
x = 0

# двоеточие - управляющий символ отступа на следующей строке (PEP8)
if x > 0:  # True/False
    print("Больше нуля!")
elif x < 0:
    print("Меньше нуля!")
else:
    print("Равно нулю!")

# # Примечание
# if True:
#     print("Выполняется всегда!")


# оператор цикла while

i = 0
while i < 10:  # True/False
    print('i =', i)
    i += 1

# Пример
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
min_price = min(room_prices)

i = 0

while i < len(room_prices):
    price = room_prices[i]
    if price == min_price:
        print(f"Найдена минимальная цена {price}")
        break
    i += 1


# Оператор цикла for
# обратимся к списку room_prices
# Вариант 1 - перебрать элементы
for elem in room_prices:
    print('Цена: ', elem)

# Вариант 2 - перебрать индексы
for ind in range(len(room_prices)):
    print('Цена: ', room_prices[ind])

# Вариант 3 - получить пары индекс-элемент
for ind, elem in enumerate(room_prices):
    print(f"Цена №{ind+1} - {elem}")
    