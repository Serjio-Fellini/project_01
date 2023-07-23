# ########################Классы на примере автомобилей########################

# Что такое экземпляр?
# Что такое класс?

# Создаем класс автомобиля
# класс - это как чертеж, по которому конвеер-интерпретатор делает новые машины-экземпляры
class Car:
    # атрибуты
    color = 'Black'
    wheels = 4
    engine_status = False

    # методы - функции внутри класса
    # связанные методы - метод с указанием имени экземпляра через параметр
    def sound(self):
        return 'Beeeb'
    
    def start_engine(self, key):
        if key == 'Ключ':
            self.engine_status = True


# Создаем экземпляры автомобиля
# экземпляр это автомобиль из серии, который живет своей жизнью

toyota_1 = Car()
toyota_2 = Car()
toyota_3 = Car()
toyota_4 = Car()
toyota_5 = Car()

# Изменим цвет автомобиля toyota_3
toyota_3.color = 'Red'
print(
    f'цвет toyota_3 - {toyota_3.color}', 
    f'цвет toyota_1 - {toyota_1.color}',
    sep='\n'
    )
# вызов метода
print(toyota_3.sound())  # почему ошибка с количеством аргументов? 
# Необходимо задать метод как связанный (добавить параметр self)

toyota_3.start_engine('Ключ')
print(toyota_3.engine_status)