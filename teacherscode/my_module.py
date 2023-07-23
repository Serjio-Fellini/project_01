# Это модуль с функциями

# структура
# 1. импорты
# 2. определение классов и функций
# 3. вызовы/тело цикла (если модуль 1)

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


def div(a, b):
    i = a
    count_div = 0

    while i > 0:
        i -= b
        count_div += 1
    return count_div


def positive_sum(lst):
    return sum([i for i in lst if i>0])


var_1 = 'Привет'

def foo():
    print('Как дела?')

# if __name__ == '__main__':
#     print('Название модуля', __name__,'\nЗапуск')





