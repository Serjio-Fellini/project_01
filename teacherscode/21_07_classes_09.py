# ########################КЛАССЫ########################

# Для создания новых объектов, создаем класс
# Пример - создадим класс ячейки из таблицы excel

# этап создания класса
# каждое слово внутри имени класса записывается с большой буквы 
#   ClassOfMyDream, MySQLClient

class Cell:
    '''Класс ячейки'''

    # методы - функции внутри класса
    # конструктор - магический метод __init__
    def __init__(self) -> None:
        # атрибуты - переменные внутри класса
        self.content = 1
        self.content_type = type(self.content)

    def set_value(self, val):
        self.content = val
        self.content_type = type(val)

# этап создания экземпляра класса
#   например: x = int()
A1 = Cell()

# вызов атрибутов экземпляра
print(A1.content)
print(A1.content_type)

# вызов метода
A1.set_value('Hello')
print(A1.content)
print(A1.content_type)


# Как изменить природу объектов в Python?
# с помощью Магии Python:
#   __init__ - присвоение объекту имени (создание переменной)
#   __str__ - приведение к строке


# Класс хранилища в облачном сервисе
class Bucket:
    '''Хранилище объектов статического сайта'''

    def __init__(self, tutorial=None) -> None:
        self.content = []
        if tutorial != None:
            self.content.append(tutorial)

    def __str__(self) -> str:
        return 'Содержимое: ' + ', '.join(self.content)
    
    def __bool__(self) -> bool:
        return self.content != []

    def add(self, obj):
        self.content.append(obj)

# создание экземпляра через __init__
website = Bucket('README.md')
website.add('index.html')

# приведение к строке через __str__
print(website)

# приведение к строке через __bool__
empty_bucket = Bucket()

print(bool(empty_bucket))
print(bool(website))


# Удаление объектов из памяти Python
# автоматическая очистка памяти после работы скрипта, через метод __del__
class Truck:
    '''Самосвал который загружает в ковш и выгружает в другом месте'''
    def __init__(self, *args):
        print('Загружено в ковш:')
        [print(f'  * {i}') for i in args]

    def __del__(self):
        print('Выгружено из ковша')

Truck('бетон', 'кирпичи', 'арматура')


# ДЗ

m = Matrix(10, 10)

# 1 1
# 1 1

# None None
# None None

# 1 2 3
# 2 4 6
# 3 6 9

# a b
# 1 2
# 2 4

class Matrix:
    def __init__(self):
        self.field = pd.DataFrame()
        