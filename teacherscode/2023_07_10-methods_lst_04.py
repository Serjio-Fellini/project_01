
# Вопросы
# Что возвращает метод insert, append и тд?
# Какие бывают методы списка?

# Задача 2
# Приведем список покупок в магазине

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом

from pprint import pprint
pprint(dir(shop_list))
lgth = len(shop_list)
print(lgth)

shop_list.insert(shop_list.index("Рис"), "Рыба")
print(shop_list)

#   b. Добавьте фрукты из списка fruits в конец списка shop_list

fruits = ['Яблоко', 'Апельсин', 'Клубника']

# # append добавляет все что угодно в конец списка
# shop_list.append(fruits)
# print(shop_list, len(shop_list))

# extend распаковывает списки в конце другого списка
shop_list.extend(fruits)
print(shop_list, len(shop_list))

#   c. Удалите из списка shop_list картофель

# # pop вытаскивает элемент по индексу, показывает и выбрасывает
# print(shop_list.pop(0))
# print(shop_list, len(shop_list))

# remove удаляет элемент из списка
shop_list.remove("Картофель")
print(shop_list, len(shop_list))

#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 

print(f"Номер хлеба в списке - {shop_list.index('Хлеб')}")