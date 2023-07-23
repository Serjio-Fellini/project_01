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


# Задача 3
# Дано 2 числа
# описать логику деления числа a на число b, не используя операции деления

a, b = 10, 2
i = a
count_div = 0

while i > 0:
    i -= b
    count_div += 1

print(f'Результат деления {a} на {b} = {count_div}')


# Задача 4

# Дан список целых чисел
# Найдите сумму всех положительных чисел внутри списка
primes = [4, 10, -17, 3, -3]

res = 0
for i in primes:
    if i > 0:
        res += i
    # else:
    #     pass

print(res)

