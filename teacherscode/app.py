# Инициализационный файл

# модуль - это файл с расширением .py
# пакет - папка с модулями, в которой присутствует __init__.py
# библиотека - набор пакетов и модулей

# импорт из другого модуля
# вариант импорта 1
import my_module
# примеры: import os

my_module.foo()

# вариант импорта 2
import my_module as mm
# примеры: import pandas as pd
print(mm.div(100, 20))

# вариант импорта 3
from ex_module import foo
# пример: from pprint import pprint, from flask import Flask
foo()


# импорт из пакета
import my_package.module_2 as m2
# примеры: import matplotlib.pyplot as plt

m2.foo_2()

# вариант импорта из подпакета
from my_package.subpackage import foo_3


# Запуск скрипта
print(
    my_module.__name__,  # my_module
    __name__,  # __main__
    sep='\n')

# Если модуля является запускаемым, то выполни что либо
if __name__ == '__main__':
    foo_3()
    print('Запуск скрипта')
