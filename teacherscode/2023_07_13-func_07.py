# ############################функции############################

# У нас есть блок кода который решает поставленную задачу
employees_1 = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
    }

employees_2 = {
    'Leo' : 110000,
    'Mike' : 60000,
    'Cristina' : 70000,
    }

# Создание функции
# Аннотация к функции
# Документирование функции
def get_topmgrs(empl_dct: dict, *, limit: int = 100000) -> list:
    """
    get_topmgrs возвращает список сотрудников,
    у котиорых зп больше прогового значения.
    По умолчанию limit = 100000.
    """
    top_mgrs = []

    for name in empl_dct:
        if empl_dct[name] >= limit:
            top_mgrs.append(name)

    return top_mgrs


# Использование результата работы функции в дургих вычислениях
# Позиционные и именованные параметры


review_1 = [employees_1[i]*1.5 for i in get_topmgrs(employees_1, limit=90000)]
review_2 = [employees_2[i]*1.5 for i in get_topmgrs(employees_2, limit=90000)]


# именованные параметры в print
print('****Начало отчета****', review_1, review_2, 
      end='\n****Конец отчета****\n', sep='\n')


# Функция - это блок кода, который можно вызывать много много раз

# создание функции
# внутри скобок указываются параметры
def greeting(name):
    return f'Привет, {name}!'


# вызов функции
# greeting()
for i in ['Марк', 'Роман', 'Мария']:
    print(greeting(i))

# Преобразуем в функции предыдущие примеры
# из задачи 3
def div(a, b):
    i = a
    count_div = 0

    while i > 0:
        i -= b
        count_div += 1
    return count_div

print(div(10, 5))

# из задачи 4
def positive_sum(lst):
    return sum([i for i in lst if i>0])

print(positive_sum([4, 10, -17, 3, -3]))

